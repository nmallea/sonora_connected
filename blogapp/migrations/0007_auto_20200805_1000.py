# Generated by Django 3.1 on 2020-08-05 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_auto_20200805_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postdetails',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]