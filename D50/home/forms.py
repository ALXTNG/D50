from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from home.models import Document
from home.models import Proposal

#this one is to format the help text
from django.utils.safestring import mark_safe



from .models import  Profile


class SignUpForm(UserCreationForm):
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required.')
    
    location = forms.CharField(max_length=30, required=False, help_text='Optional.')
    institution = forms.CharField(max_length=500, required=False, help_text='Optional.')
    role = forms.CharField(max_length=500, required=False, help_text='Optional.')    
    
    
    committe_member_verification = forms.BooleanField( label='Committee', help_text=mark_safe('Tick this box if you are a NeXT Committe Member.<br /> This will grant you access to the submitted proposals and internal documentation. <br /> <i><small>Please note that your request will remain pending until it receives approval from the webmaster. </small></i> '),required=False)
    collaborator_verification = forms.BooleanField( label='Collaborator', help_text=mark_safe('Tick this box if you are a NeXT Collaborator. <br /> This will grant you access to internal documentation. <br /> <i><small>Please note that your request will remain pending until it receives approval from the webmaster. </small></i> '), required=False)
    
    notes_status = forms.CharField(max_length=500, required=False, help_text='Please add here any explanation you might want to provide about the status of Collaborator or Committee Member')

    
    
    

    class Meta:
        model = User
        #~ exclude = ('committe_member_verification', 'collaborator_verification','notes_status')

        fields = ('username', 'last_name', 'first_name', 'institution','location', 'role','email', 'password1', 'password2', )
        #~ fields = ('username', 'email', 'password1', 'password2', )


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('institution', 'location', 'role')

    
#~ class UserForm(forms.ModelForm):
    #~ class Meta:
        #~ model = User
        #~ fields = ('first_name', 'last_name', 'email')

#~ class ProfileForm(forms.ModelForm):
    #~ class Meta:
        #~ model = Profile
        #~ fields = ('url', 'location', 'company')    
    
class UpdateProfile(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user    


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
        
        
class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = ('proposal_rationale', 'proposal_technical_support','proposal_title', 'comments')
        
class ProposalFormEdit(forms.ModelForm):


    class Meta:
        model = Proposal
        fields = ('proposal_rationale', 'proposal_technical_support','proposal_title', 'comments')
        
    #~ proposal_rationale = forms.FileField(required = False)
    #~ proposal_technical_support = forms.FileField(required = False)
    def __init__(self, *args, **kwargs):
        super(ProposalFormEdit, self).__init__(*args, **kwargs)
        self.fields['proposal_rationale'].required = False
        self.fields['proposal_technical_support'].required = False
    
        
    #~ form_proposal_rationale =  forms.FileField( required=True, help_text='this is the rationale of the proposal')
    #~ form_proposal_technical_support =  forms.FileField(required=True, help_text='this is the technical addendum of the proposal')
    #~ form_comments=  forms.CharField(max_length=1000, required=False)
