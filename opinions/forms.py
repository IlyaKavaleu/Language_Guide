from django import forms

from opinions.models import Opinion


class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opinion
        fields = ['text', 'rating', ]
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'rating': forms.Select(
                choices=[(1, '1 звезда'), (2, '2 звезды'), (3, '3 звезды'), (4, '4 звезды'), (5, '5 звезд')]), }
