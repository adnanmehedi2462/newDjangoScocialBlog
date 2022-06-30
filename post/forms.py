
from django import forms
from USER.models import Profile
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class editpostform(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','content','image']
    