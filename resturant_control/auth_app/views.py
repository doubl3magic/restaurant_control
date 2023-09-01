from django.shortcuts import redirect
from django.contrib.auth import views as auth_views, logout
from django.urls import reverse_lazy
from django.views import generic as views

from resturant_control.auth_app.forms import CreateProfileForm


# TODO
class CreateProfileView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'auth_app/register.html'
    success_url = reverse_lazy('login')


class LoginView(auth_views.LoginView):
    template_name = 'auth_app/login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


def user_log_out(request):
    logout(request)
    return redirect('home')
