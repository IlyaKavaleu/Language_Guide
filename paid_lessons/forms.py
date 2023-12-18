from django import forms
from paid_lessons.models import PaidLesson, PaidСhapter


class PaidLessonForm(forms.ModelForm):
    class Meta:
        model = PaidLesson
        fields = ['title', 'description', 'price', 'duration', 'video_url', ]
        widgets = {'description': forms.Textarea(attrs={'cols': 64})}


class AddChapterForm(forms.ModelForm):
    class Meta:
        model = PaidСhapter
        fields = ['title', 'description', 'duration', 'video_url', ]
        widgets = {'description': forms.Textarea(attrs={'cols': 64})}
