# Generated by Django 3.0.2 on 2020-02-24 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0005_auto_20200224_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewshedulemodel',
            name='selectempid',
            field=models.IntegerField(unique=True),
        ),
    ]
