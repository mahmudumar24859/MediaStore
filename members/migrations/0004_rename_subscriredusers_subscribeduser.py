# Generated by Django 4.0.3 on 2023-03-06 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_subscriredusers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SubscriredUsers',
            new_name='SubscribedUser',
        ),
    ]
