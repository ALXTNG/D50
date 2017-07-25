from django.shortcuts import render, redirect

from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import *
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
 
from django.contrib.auth.models import User

from django.contrib import messages

#to allow for password change
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# email verification
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text
from django.template.loader import render_to_string
from home.forms import SignUpForm
from home.tokens import account_activation_token
from django.core.mail import send_mail
from django.core.mail import EmailMessage # this one is the extended version (e.g. attachements)



from .models import  Post
from .models import  Proposal
from .models import  Profile
from django.contrib.auth.models import User

from .forms import *

#this one is to import the form from home
from home.forms import SignUpForm

#this is to allow for the decorator @transaction.atomic
from django.db import transaction

# for the uploads:
from django.conf import settings
from django.core.files.storage import FileSystemStorage



def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
    
    
def index(request):
    post_list = Post.objects.order_by('-pub_date')[:]
    context = {'post_list': post_list}
    return render(request, 'home/index.html', context)
    
 
def signup(request):

    if request.method == 'POST':
      #~ This on is to sue default one
        #~ form = UserCreationForm(request.POST)
        #~ thisone is to use our own (in forms.py in) home
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False            

            #~ user.save()
 
            user.save()           
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.location = form.cleaned_data.get('location')
            user.profile.institution = form.cleaned_data.get('institution')
            user.profile.role = form.cleaned_data.get('role')
            user.save()           

            # below is the email activation bit
            current_site = get_current_site(request)
            subject = 'Activate your NeXT-Grenoble account'
            message = render_to_string('home/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            #~ user.email_user(subject, message)
            send_mail(subject, message, 'no-reply-NeXT@next-grenoble.fr', [user.email])
            return redirect('account_activation_sent')
                       
            #old version without email activation. Upside: directly logs you in          
            #~ raw_password = form.cleaned_data.get('password1')
            #~ user = authenticate(username=user.username, password=raw_password)
            #~ login(request, user)

            #~ return redirect('../../')
    else:
      #~ Same
        form = SignUpForm()
        #~ form = UserCreationForm()
    return render(request, 'home/signup.html', {'form': form})

#def signup(request):
#    if request.method == 'POST':
#        form = SignUpForm(request.POST)
#        if form.is_valid():
#            user = form.save()
#            user.refresh_from_db()  # load the profile instance created by the signal
#            user.profile.location = form.cleaned_data.get('location')
#            user.profile.institution = form.cleaned_data.get('institution')
#            user.profile.role = form.cleaned_data.get('role')
#            user.save()
#            raw_password = form.cleaned_data.get('password1')
#            user = authenticate(username=user.username, password=raw_password)
#            login(request, user)
#            
#            return redirect('home')
#    else:
#        form = SignUpForm()
#    return render(request, 'home/signup.html', {'form': form})
#    
#    

#~ def view_profile(request):
    #~ profile = request.user.get_profile()    

#~ def edit_profile(request):
    #~ template_var = {}
    #~ if '_auth_user_id' in request.session:
        #~ userId = request.session['_auth_user_id']
        #~ new_profile_user = Profile.objects.get(user_id=userId)
        #~ userDetails = User.objects.get(pk=userId)
        #~ if request.method == 'POST':
            #~ userDetails.first_name = request.POST['first_name']
            #~ userDetails.email = request.POST['email']
            #~ userDetails.save()
    #~ template_var['new_profile_user']=new_profile_user
    #~ return render_to_response('home/edit_user.html',template_var,)
    
    
#the stuff below is for later updates
@login_required
#this decorator is to handle safe database transactions (usally run in autocommit mode, i.e each query is immediately committed to the database)
# transactions are used to guarantee the integrity of ORM operations that require multiple queries, especially delete() and update() queries.  
#It works like this. Before calling a view function, Django starts a transaction. If the response is produced without problems, Django commits the transaction. If the view produces an exception, Django rolls back the transaction. ensuring atomicity, i.e. that 
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('home')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'home/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
    
    
@login_required
def user_status(request):
    return render(request, 'home/user_status.html')
        

        
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('update_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'home/change_password.html', {
        'form': form
    })

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'home/account_activation_invalid.html')

def account_activation_sent(request):
    return render(request, 'home/account_activation_sent.html')

#~ def simple_upload(request):
    #~ if request.method == 'POST' and request.FILES['myfile']:
        #~ myfile = request.FILES['myfile']
        #~ fs = FileSystemStorage()
        #~ filename = fs.save(myfile.name, myfile)
        #~ uploaded_file_url = fs.url(filename)
        #~ return render(request, 'home/simple_upload.html', {
            #~ 'uploaded_file_url': uploaded_file_url
        #~ })
    #~ return render(request, 'home/simple_upload.html')
    
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            
            return redirect('proposal_succesfully_uploaded')
    else:
        form = DocumentForm()

    return render(request, 'home/model_form_upload.html', {
        'form': form
    })

@login_required    
@transaction.atomic    
def proposal_edit(request, oid):
    proposal_id_requested = Proposal.objects.get(id=oid)

    if request.method == 'POST':
        form = ProposalForm(request.POST, request.FILES, instance=proposal_id_requested)
        if form.is_valid():
            record = form.save(commit=False)
            form.save()
            
            #below is the email sending bit 
            user_loggedin = request.user.get_username()
            first_name = request.user.first_name
            last_name = request.user.last_name
            email_user_logged_in = request.user.email
            comments = form.cleaned_data['comments']
            if len(comments)>0: comments_exist=True
            else: comments_exist=False
            #~ rationale = form.cleaned_data['proposal_rationale']
            #~ technical_support = form.cleaned_data['proposal_technical_support']
            
            #~ technical_support1 = request.FILES['proposal_technical_support']
            #~ rationale1 = request.FILES['proposal_rationale']
            
            title = form.cleaned_data['proposal_title']
            #~ text 
            subject = 'Successful proposal modification at NeXT from %s'%user_loggedin
            
            current_site = get_current_site(request)

            message = render_to_string('home/edited_proposal_email.html', {
                'user': user_loggedin,
                'first_name': first_name,
                'last_name': last_name,
                'title':title,
                'comments':comments,
                'comments_exist':comments_exist,
                'domain': current_site.domain,

            })
            #~ user.email_user(subject, message)
            
            finalemail = EmailMessage(
            subject,
            message,
            'proposal-submitted-noreply@next-grenoble.fr',
            [email_user_logged_in],
            ['contact@next-grenoble.fr'],
            reply_to=['contact@next-grenoble.fr'],
)

            #~ message.attach('proposal_rationale.pdf', rationale , 'image/png')
            #~ file_adress  =current_site.domain+record.proposal_rationale.url
            finalemail.attach_file(record.proposal_rationale.path)
            finalemail.attach_file(record.proposal_technical_support.path)
            #~ finalemail.attach(rationale.name, rationale.read(), rationale.content_type)
            #~ finalemail.attach(rationale.name, response, rationale.content_type)
            #~ finalemail.attach_file(rationale1)
            #~ finalemail.attach_file(technical_support1)
            finalemail.send()
            #~ send_mail(subject, message, 'proposal-submitted-noreply@next-grenoble.fr', [email_user_logged_in,'contact@next-grenoble.fr'])
            #~ request.user.profile.proposals.add(record)
            #~ form.save()
            return redirect('proposal_succesfully_uploaded')
            
            
            
            return redirect('user_status')
        else:
          messages.error(request, ('Please correct the error below.'))    
    else:
        form = ProposalForm(instance=proposal_id_requested)
    return render(request, 'home/proposal_form_edit.html', {
        'form': form
    })

@login_required
def list_proposals(request):
    proposal_list = Proposal.objects.all()
    context = {'proposals':proposal_list}
    return render(request, 'home/list_of_proposals.html', context)
    
    
@login_required    
def proposal_view(request, oid):
    proposal_id_requested = Proposal.objects.get(id=oid)
    return render(request, 'home/proposal_view.html', {
        'proposal_id_requested': proposal_id_requested
    })
    
@login_required    
def profile_view(request, oid):
    profile_id_requested = User.objects.get(id=oid)
    return render(request, 'home/profile_view.html', {
        'profile_id_requested': profile_id_requested
    })
    
@login_required
def list_profiles(request):
    profile_list = User.objects.all()
    context = {'profiles':profile_list}
    return render(request, 'home/list_of_profiles.html', context)
    
        
@login_required    
def proposal_form_upload(request):
    #~ user_proposal=model.user.objects.get(pk=)
    
    if request.method == 'POST':
        form = ProposalFormEdit(request.POST, request.FILES)
        if form.is_valid():
            record = form.save(commit=False)
            record.user_proposal = request.user.get_username()
            record.save()
            
            #adding this proposal to the user (many to many)
            request.user.profile.proposals.add(record)
            
            #below is the email sending bit 
            user_loggedin = request.user.get_username()
            first_name = request.user.first_name
            last_name = request.user.last_name
            email_user_logged_in = request.user.email
            comments = form.cleaned_data['comments']
            if len(comments)>0: comments_exist=True
            else: comments_exist=False
            #~ rationale = form.cleaned_data['proposal_rationale']
            #~ technical_support = form.cleaned_data['proposal_technical_support']
            
            #~ technical_support1 = request.FILES['proposal_technical_support']
            #~ rationale1 = request.FILES['proposal_rationale']
            
            title = form.cleaned_data['proposal_title']
            #~ text 
            subject = 'Successful proposal submission at NeXT from %s'%user_loggedin
            
            current_site = get_current_site(request)

            message = render_to_string('home/submitted_proposal_email.html', {
                'user': user_loggedin,
                'first_name': first_name,
                'last_name': last_name,
                'title':title,
                'comments':comments,
                'comments_exist':comments_exist,
                'domain': current_site.domain,

            })
            #~ user.email_user(subject, message)
            
            finalemail = EmailMessage(
            subject,
            message,
            'proposal-submitted-noreply@next-grenoble.fr',
            [email_user_logged_in],
            ['contact@next-grenoble.fr'],
            reply_to=['contact@next-grenoble.fr'],
)

            #~ message.attach('proposal_rationale.pdf', rationale , 'image/png')
            #~ file_adress  =current_site.domain+record.proposal_rationale.url
            finalemail.attach_file(record.proposal_rationale.path)
            finalemail.attach_file(record.proposal_technical_support.path)
            #~ finalemail.attach(rationale.name, rationale.read(), rationale.content_type)
            #~ finalemail.attach(rationale.name, response, rationale.content_type)
            #~ finalemail.attach_file(rationale1)
            #~ finalemail.attach_file(technical_support1)
            finalemail.send()
            #~ send_mail(subject, message, 'proposal-submitted-noreply@next-grenoble.fr', [email_user_logged_in,'contact@next-grenoble.fr'])
            #~ request.user.profile.proposals.add(record)
            #~ form.save()
            return redirect('proposal_succesfully_uploaded')
    else:
        form = ProposalFormEdit()
    return render(request, 'home/proposal_form_upload.html', {
        'form': form
    })
    
@login_required    
def proposal_succesfully_uploaded(request):
  return render(request, 'home/proposal_succesfully_uploaded.html')
