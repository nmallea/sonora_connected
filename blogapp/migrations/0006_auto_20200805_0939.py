# Generated by Django 3.1 on 2020-08-05 04:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0005_postdetails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postdetails',
            name='voters',
        ),
        migrations.AddField(
            model_name='postdetails',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='postdetails',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
