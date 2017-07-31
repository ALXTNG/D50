from django.shortcuts import render
from django.http import HttpResponse
from .models import FilesUploaded

from django.contrib.auth.decorators import user_passes_test

def forumtest(user):
    return user.is_authenticated() and user.has_perm("home.can_see_forum")
    
def WIP(request):
    return render(request, 'workinprogress/WIP.html')
    
def access_forbidden(request):
    return render(request, 'workinprogress/permission_denied.html')
    
def access_forbidden_forum(request):
    return render(request, 'workinprogress/forum_beta.html')

def aboutNEXT(request):
    return render(request, 'workinprogress/aboutNEXT.html')
    
def aboutwebsite(request):
    return render(request, 'workinprogress/aboutwebsite.html')
    
def logo(request):
    return render(request, 'workinprogress/logo.html')
    
def contact(request):
    return render(request, 'workinprogress/contact.html')
    
def mailinglist(request):
    return render(request, 'workinprogress/mailinglist.html')
    
def neutron_x_ray_matter(request):
    return render(request, 'workinprogress/neutron_x_ray_matter.html')

#~ @user_passes_test(D50test, login_url="/login/")
def D50(request):
    return render(request, 'workinprogress/D50.html')
    
def proposalDetails(request):
  
    file_list = FilesUploaded.objects.all()
    pdf_file = FilesUploaded.objects.filter(title__icontains="form")
    context = {'file_list': file_list, 'pdf_file' : pdf_file }
    return render(request, 'workinprogress/proposalDetails.html', context)
    
def downloadForm(request):
    # Create the HttpResponse object with the appropriate headers.
    pdf_file = FilesUploaded.objects.filter(title__icontains="pdfform")
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Type'] = 'application/pdf'
    response['Content-Disposition'] = 'attachment; filename="NeXT_ProposalSubmissionForm.pdf"'
    return response

#~ def index(request):
    #~ return HttpResponse("Hello, world. You're at the polls index.")
