from django.contrib import admin

# the two ones below are to visualize user features in Django 
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# this is to import the profile of the users
from .models import Profile


# Register your models here.
from .models import Post
from .models import Proposal
from .models import Proposal_round
from .models import Document
from .models import Tag

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Proposal)
admin.site.register(Proposal_round)
admin.site.register(Document)

# we are using an inline model in brief is the ability to edit a model + its parent (e.g. a profile and a user profile) in the same page!
#https://docs.djangoproject.com/en/1.11/ref/contrib/admin/#inlinemodeladmin-objects
#https://simpleisbetterthancomplex.com/tutorial/2016/11/23/how-to-add-user-profile-to-django-admin.html
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    
    # this one below is to override the the list display of the user admin too add more fields from the user Profile
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_institution', 'is_email_confirmed')
    list_select_related = ('profile', )

    def get_institution(self, instance):
        return instance.profile.institution
    get_institution.short_description = 'Institution'
    
    def is_email_confirmed(self, instance):
        return instance.profile.email_confirmed
    is_email_confirmed.short_description = 'is email confirmed'
    

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)
#this is to unregister the old User admin and register the new one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
