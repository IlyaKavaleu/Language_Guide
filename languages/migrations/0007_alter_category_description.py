# Generated by Django 4.2.7 on 2023-12-05 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0006_alter_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=25000, unique=True),
        ),
    ]