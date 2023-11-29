from django.db import models
from django.contrib.auth.models import User
from languages.models import Language


class Comments(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'{self.user}____{self.text}'
