# Generated by Django 4.0 on 2022-04-01 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_signup_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='emal',
        ),
    ]
