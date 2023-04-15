from django import forms
from accounts.models import InstagramUser

class UserForm(forms.ModelForm):
    class Meta:
        model = InstagramUser
        fields = ['username', 'password']