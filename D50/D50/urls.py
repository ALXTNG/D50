"""D50 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from home import views as core_views


from django.conf.urls import include,url
import home.views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^workinprogress/', include('workinprogress.urls')),
    
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', home.views.logout_page, name = 'logout_page'),
    
    url(r'^edit_profile/$', home.views.update_profile, name = 'update_profile'),
    url(r'^user_status/$', home.views.user_status, name = 'user_status'),
    url(r'^password/$', home.views.change_password, name='change_password'),
    #~ url(r'^register/', home.views.register, name='register'),
    
    url(r'^signup/$', home.views.signup, name='signup'),
        
    #account activation
    url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        core_views.activate, name='activate'),
    
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    
    #upload
    url(r'^proposal_upload/$', home.views.proposal_form_upload, name='proposal_upload'),
    url(r'^proposal_edit/(?P<oid>\d+)/$$', home.views.proposal_edit, name='proposal_edit'),
    #~ url(r'^proposal_edit/$', home.views.proposal_edit, name='proposal_edit'),
    url(r'^proposal_succesfully_uploaded/$', home.views.proposal_succesfully_uploaded, name='proposal_succesfully_uploaded'),
    url(r'^upload/$', home.views.model_form_upload, name='model_form_upload'),
    
    url(r'^list_proposals/$', home.views.list_proposals, name='list_proposals'),
    url(r'^proposal_view/(?P<oid>\d+)/$', home.views.proposal_view, name='proposal_view'),
    
    url(r'^list_profiles/$', home.views.list_profiles, name='list_profiles'),
    url(r'^profile_view/(?P<oid>\d+)/$', home.views.profile_view, name='profile_view'),


    url(r'^$', include('home.urls'))]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
