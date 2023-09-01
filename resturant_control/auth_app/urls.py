from django.urls import path

from resturant_control.auth_app.views import CreateProfileView, LoginView, user_log_out

urlpatterns = [
    path('register/', CreateProfileView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', user_log_out, name='logout')
]