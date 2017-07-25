from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime
from django.template.defaultfilters import slugify # this one is to substitute '-' to spaces in the slug field

#need this bit to extend the user model and have a User Profile.
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver



# here I'm hardcoding some users groups if they do not exist...not great but that will do for the time being...
from django.contrib.auth.models import Group, Permission
Users_proposers_basic, created = Group.objects.get_or_create(name='Users_proposers_basic')
Collaborators, created = Group.objects.get_or_create(name='Collaborators')
commitee_member, created = Group.objects.get_or_create(name='commitee_member')
commitee_president, created = Group.objects.get_or_create(name='commitee_president')

#~ from django.contrib.auth.models import User, Group, Permission
#~ from django.contrib.contenttypes.models import ContentType

#~ content_type = ContentType.objects.get(app_label='myapp', model='BlogPost')
#~ permission = Permission.objects.create(codename='can_publish',
                                       #~ name='Can Publish Posts',
                                       #~ content_type=content_type)
#~ user = User.objects.get(username='duke_nukem')
#~ group = Group.objects.get(name='wizard')
#~ group.permissions.add(permission)
#~ user.groups.add(group)

# here I create arbitrary permissions:

#this one is for the creation of the Profile model whenever a new user is created. 
from django.db.models.signals import post_save
from django.dispatch import receiver


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True, null=False)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):  # __unicode__ for Python 2
      return self.description
    
    
class Tag(models.Model):
  tag = models.CharField(max_length=200)      
  def __unicode__(self):
        return self.tag
        
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle=models.TextField( blank=True, help_text='expand on the title')
    text = models.TextField( blank=True, help_text='add text')
    extended_description=models.TextField( blank=True, help_text='expand some more if needed')
    email_confirmed = models.BooleanField(default=False)

    #~ slug = models.CharField('slug', max_length=150, unique=True, editable=False , help_text='do not change please') # the editable=False is to avoid admins from writing the slug, which is instead auto-generated -- see below.
    # this one is a unique -in this case- tag one can use for referencing the post I do not want to use the Slugfield to copy the url structure of https://www.djangorocks.com/snippets/creating-a-unique-slug.html
    
    pub_date = models.DateTimeField('date published', help_text='add date that will be displayed and used for sorting')
    image = models.ImageField(upload_to='./', max_length=500, blank=True, null=True, help_text='add image that will be displayed')
    tag = models.ManyToManyField(Tag, related_name='tag_post', help_text='add here tags if tags if useful. if they do not exist, click on plus symbol.')
    urllink = models.URLField(max_length=200, blank=True, null=True, help_text='add here link to multimedia materials (maps, videos). Make sure to use the embeddable version and not just the standard link')
    def __unicode__(self):
        return self.title
        
    #~ # this effectively REDEFINES the save command (which already exists) so that when you save after adding a post yo also do the other actions in this bit.
    #~ #    
    #~ def save(self):
        #~ super(Post, self).save() # use save command from parent class
        #~ date = datetime.date.today()
        #~ self.slug = '%i/%i/%i/%s' % ( # define the slug as a combination of date the id and the slugified ( substitute '-' to spaces ) title
            #~ date.year, date.month, date.day, slugify(self.title)
        #~ )
        #~ super(Post, self).save() # re-use save command from parent class
    
    # this function allows for which as of 2013 is preferrable to the  @permalink decorator (http://stackoverflow.com/questions/13503645/what-is-permalink-and-get-absolute-url-in-django)
    def get_absolute_url(self):
        return reverse('mymodel_detail', args=(self.slug,))

class Proposal_round(models.Model):
    proposal_round = models.IntegerField(default=0, null=True)
    def __str__(self):  # __unicode__ for Python 2
      return str(self.proposal_round)

class Proposal(models.Model):

    proposal_rationale =  models.FileField(upload_to='proposals/', blank=False, null=False, help_text='this is the rationale of the proposal')
    proposal_technical_support =  models.FileField(upload_to='proposals/', blank=False, null=False, help_text='this is the technical addendum of the proposal')
    
    comments =  models.CharField(max_length=1000, blank=True, help_text='add comments, if any')
    proposal_title = models.CharField(max_length=1000, blank=False, help_text='Please insert the title of the proposal')
    
    response_scientific_committee =  models.TextField( blank=True, help_text='add text')
    response_steering_committee = models.TextField( blank=True, help_text='add text')
    
    
    proposal_round= models.ForeignKey(Proposal_round, on_delete=models.SET_NULL, null=True)
    
    #~ proposal_userID=models.CharField(max_length=1000, blank=True, help_text='add comments, if any')
    
    proposal_progressive_index = models.IntegerField(default=0)
    datetime = models.DateTimeField(default=datetime.datetime.now)
    #~ user_proposal = models.ForeignKey(User, null=True)
    user_proposal = models.CharField(max_length=1000, null=True, help_text='NeXT username of the proposer', verbose_name='Name of the proposer')
    proposal_ID= models.CharField(max_length =100, null=True, verbose_name='code_of_the_proposal')
    
    def save(self):
        if Proposal.objects.exists(): # for the first case!
          self.proposal_progressive_index = Proposal.objects.order_by('proposal_progressive_index').last().proposal_progressive_index + 1
          #~ print self.proposal_progressive_index
          # just taking the last possible round at the moment...maybe make a bit smater?
        else:
          self.proposal_progressive_index = 0 
        
        if Proposal_round.objects.exists():
          self.proposal_round = Proposal_round.objects.order_by('proposal_round').last()
        else:
          PR = Proposal_round(proposal_round=3) # if it doen't exist, I'll just create one...starting from 3 (the first one online...)
          PR.save() # then I need to save this instance
          self.proposal_round = Proposal_round.objects.order_by('proposal_round').last()
          surname = self.proposal_set.all().last_name


        #~ self.proposal_ID = '{0:0>3}-{1:0>3}-{2}'.format(self.proposal_round,self.proposal_progressive_index, self.profile_of_proposal.values("location"))

        self.proposal_ID = '{0:0>3}-{1:0>3}-{2}'.format(self.proposal_round,self.proposal_progressive_index, self.user_proposal)
        super(Proposal, self).save()

        
    def __str__(self):  # __unicode__ for Python 2
      return str(self.proposal_ID)
      

    
    
    
        
#bit from https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone  
#https://coderwall.com/p/ktdb3g/django-signals-an-extremely-simplified-explanation-for-beginners      
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)

    location = models.CharField(max_length=30, blank=True)
    institution = models.TextField(max_length=500, blank=True)
    role = models.TextField(max_length=500, blank=True)
    proposals = models.ManyToManyField(Proposal, related_name='profile_of_proposal', help_text='this is for the proposals')

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username
    class Meta:
        permissions = (
            ("can_see_forum", "Can see forum"),
            ("cann_see_repository", "Can vote in elections"),
            ("can_see_some_of_our_results", "Can see some of our results"),
            ("can_see_private_files", "Can see private_files"),
            ("can_see_all_proposals", "Can see all proposals"),
            ("can_write_comments_on_proposals", "Can write comments on proposals"),
        )
        

    
    
    
    
    
    

# the @ receiver decorator listens to special signals of python andspecifically this one is setup to activate when post_save occurrs and more specifically when the sender is teh User function.
#https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
# when that happens, it creates (or modifies) the profile.
        
#~ @receiver(post_save, sender=User)
#~ def create_user_profile(sender, instance, created, **kwargs):
    #~ if created:
        #~ Profile.objects.create(user=instance)
    #~ instance.profile.save()

#~ @receiver(post_save, sender=User)
#~ def save_user_profile(sender, instance, **kwargs):
    #~ instance.profile.save()      
    


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
        

