# Generated by Django 4.2.7 on 2023-12-05 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0004_alter_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=15000, unique=True),
        ),
    ]