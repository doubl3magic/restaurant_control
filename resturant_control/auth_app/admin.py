from django.contrib import admin
from django.contrib.auth import get_user_model

from resturant_control.auth_app.models import Profile

UserProfile = get_user_model()


@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'date_joined')
    search_fields = ('username',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user')
