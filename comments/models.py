from django.conf import settings
from django.db import models
from programming_guide.settings import AUTH_USER_MODEL
from languages.models import Language
from django.contrib.admin import ModelAdmin


class Comments(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.user}, {self.text}'

