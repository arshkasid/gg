# Generated by Django 4.0 on 2022-04-01 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_exampleinputpassword1_contact_pass2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='exampleInputEmail1',
            new_name='email',
        ),
    ]
