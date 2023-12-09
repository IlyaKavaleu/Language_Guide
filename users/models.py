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
    country = models.CharField(max_length=100, blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    person_gender = models.IntegerField(choices=[(1, 'MAN'), (2, 'WOMAN')])
    age = models.IntegerField(null=True, blank=True)
    family_status = models.IntegerField(choices=[(1, 'Married'), (2, 'Not married')])
