from django.db import models
from programming_guide.settings import AUTH_USER_MODEL


class Message(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
