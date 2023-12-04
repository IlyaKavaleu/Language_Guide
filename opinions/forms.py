from django import forms

from opinions.models import Opinion


class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ['text', ]