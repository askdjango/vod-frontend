from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    url(r'^signup/$', views.SignupFormView.as_view(), name='signup'),
    url(r'^login/$', login, name='login', kwargs={'template_name': 'accounts/login.html'}),
    url(r'^profile/$', views.profile, name='profile'),
]

