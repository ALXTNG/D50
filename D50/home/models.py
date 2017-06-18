from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime
from django.template.defaultfilters import slugify # this one is to substitute '-' to spaces in the slug field



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
