# Generated by Django 5.1.1 on 2024-10-06 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChatApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='Message',
            new_name='message',
        ),
    ]
