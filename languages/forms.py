from django import forms

from languages.models import Category, Language


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'image']
        widgets = {'description': forms.Textarea(attrs={'cols': 80})}


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name', 'description', 'image']
        widgets = {'description': forms.Textarea(attrs={'cols': 80})}
