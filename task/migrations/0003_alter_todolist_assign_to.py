# Generated by Django 3.2.19 on 2023-05-24 08:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0002_auto_20230524_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='assign_to',
            field=models.ManyToManyField(related_name='assign_to', to=settings.AUTH_USER_MODEL),
        ),
    ]
