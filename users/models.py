from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    registered = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='image/avatars', null=True, blank=True)
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_set', blank=True)
    address = models.CharField(max_length=200, blank=False, null=False)
    instagram = models.CharField(max_length=100, blank=False, null=False)
    facebook = models.CharField(max_length=100, blank=False, null=False)
    linkedin = models.CharField(max_length=100, blank=False, null=False)
    country = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    age = models.IntegerField(null=True, blank=True)
    status_private_user_info = models.CharField(max_length=200)

    PERSON_STATUS_CHOICES = [
        ('Му', 'MAN'),
        ('WOMAN', 'WOMAN'),
    ]
    person_gender = models.CharField(max_length=20, choices=PERSON_STATUS_CHOICES, null=False, blank=False)

    FAMILY_STATUS_CHOICES = [
        ('married', 'Married'),
        ('not married', 'Not married'),
    ]
    family_status = models.CharField(max_length=20, choices=FAMILY_STATUS_CHOICES, null=False, blank=False)

    def __str__(self):
        return self.username