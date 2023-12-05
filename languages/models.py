from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=1000, unique=True)
    image = models.ImageField(upload_to='media/image/', blank=True, null=True)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        """In this class,
        we sort by name and correctly set the name in the admin panel"""
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def increment_views(self):
        self.views += 1
        self.save()

    def __str__(self):
        return self.name




class Language(models.Model):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/image/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """In this class,
         we sort by name and correctly set the name in the admin panel"""
        ordering = ('name',)
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        """Return a string representation of the name
        for in the admin panel"""
        return self.name
