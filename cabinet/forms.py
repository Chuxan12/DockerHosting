from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'about_user', 'user_image', 'wallet')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'about_user', 'user_image', 'wallet')


class ImageLinkForm(forms.Form):
    docker_image_link = forms.CharField(required=True, min_length=2)
    selected_container_id = forms.CharField(required=True, min_length=2)
