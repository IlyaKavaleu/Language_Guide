# Generated by Django 4.2.7 on 2023-12-05 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=models.TextField(max_length=500),
        ),
    ]