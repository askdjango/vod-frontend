from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as AuthLoginView
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView


class SignupFormView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup_form.html'
    success_url = settings.LOGIN_URL

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            return JsonResponse({'next_url': self.get_success_url()})
        return resposne

    def get_template_names(self):
        if self.request.is_ajax():
            return ['accounts/_signup_form.html']
        return ['accounts/signup_form.html']


class LoginView(AuthLoginView):
    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            return JsonResponse({'next_url': self.get_success_url()})
        return resposne

    def get_template_names(self):
        if self.request.is_ajax():
            return ['accounts/_login.html']
        return ['accounts/login.html']


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

