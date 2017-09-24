from django.conf import settings
from django.conf.urls import url
from django.contrib.auth.views import logout
from . import views

urlpatterns = [
    url(r'^signup/$', views.SignupFormView.as_view(), name='signup'),
    url(r'^login/$', views.LoginView.as_view(), name='login', kwargs={'template_name': 'accounts/login.html'}),
    url(r'^logout/$', logout, name='logout', kwargs={'next_page': settings.LOGIN_URL}),
    url(r'^profile/$', views.profile, name='profile'),
]

