# Generated by Django 4.2.7 on 2023-12-07 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opinions', '0002_rename_time_opinion_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='opinion',
            name='rating',
            field=models.IntegerField(choices=[(1, '1 звезда'), (2, '2 звезды'), (3, '3 звезды'), (4, '4 звезды'), (5, '5 звезд')], default=1),
            preserve_default=False,
        ),
    ]