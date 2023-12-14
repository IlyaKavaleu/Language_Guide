from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content', ]
        widgets = {
            'content': forms.Textarea(attrs={'style': 'width: 50%; height: 30px;'}),
        }