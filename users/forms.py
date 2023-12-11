from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import User


class ExtendedUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UserEditForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.help_text = None

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'image',
                  'address', 'instagram', 'facebook', 'linkedin', 'country', 'city',
                  'person_gender', 'age', 'family_status']
        widgets = {
            'person_gender': forms.Select(
                choices=[{1: 'MAN'}, {2, 'WOMAN'}]),
            'family_status': forms.Select(
                choices=[{'Married', 'Married'}, {'Not married', 'Not married'}]),
        }
        exclude = ['password1', 'password2', ]

