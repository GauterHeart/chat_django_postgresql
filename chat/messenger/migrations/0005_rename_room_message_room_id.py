# Generated by Django 3.2.5 on 2021-07-11 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0004_rename_messages_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='room',
            new_name='room_id',
        ),
    ]
