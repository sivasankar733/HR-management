# Generated by Django 3.0.2 on 2020-02-22 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0003_auto_20200218_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewsheduleModel',
            fields=[
                ('applicantid', models.IntegerField(primary_key=True, serialize=False)),
                ('selectempid', models.IntegerField(unique=True)),
                ('sheduedate', models.DateField(help_text='yyyy-mm-dd')),
            ],
        ),
    ]
