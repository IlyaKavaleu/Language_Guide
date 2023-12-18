from django.db import models
from django.db import models
from programming_guide.settings import AUTH_USER_MODEL


class PaidLesson(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок урока')
    description = models.TextField(verbose_name='Описание урока')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    duration = models.DurationField(verbose_name='Длительность урока')
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    teacher = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Преподаватель')
    video_url = models.FileField(upload_to='media/paid_lessons_video', blank=True, null=True,
                                 verbose_name='Ссылка на видео')

    def __str__(self):
        return self.title


class PaidСhapter(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок раздела')
    lesson = models.ForeignKey(PaidLesson, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание раздела')
    duration = models.DurationField(verbose_name='Длительность раздела')
    date_published = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    video_url = models.FileField(upload_to='media/paid_lessons_video', blank=True, null=True,
                                 verbose_name='Ссылка на видео')

    def __str__(self):
        return self.title
