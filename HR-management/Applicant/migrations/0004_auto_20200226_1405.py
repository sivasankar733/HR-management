# Generated by Django 3.0.2 on 2020-02-26 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Applicant', '0003_auto_20200226_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicationmodel',
            old_name='gende',
            new_name='gend',
        ),
    ]
