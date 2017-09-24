from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView


class SignupFormView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup_form.html'
    success_url = settings.LOGIN_URL


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

