from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from resturant_control.auth_app.models import Profile


class CreateProfileForm(auth_forms.UserCreationForm):
    first_name = forms.CharField(
        min_length=Profile.FIRST_NAME_MIN_LEN,
        max_length=Profile.FIRST_NAME_MAX_LEN,
    )

    last_name = forms.CharField(
        min_length=Profile.LAST_NAME_MIN_LEN,
        max_length=Profile.LAST_NAME_MAX_LEN,
    )

    picture = forms.ImageField()

    date_of_birth = forms.DateField()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'picture', 'date_of_birth')

    def __init__(self, *args, **kwargs):
        super(CreateProfileForm, self).__init__(*args, **kwargs)
        self.fields['picture'].required = False


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()

    class Meta:
        model = Profile
        fields = ()