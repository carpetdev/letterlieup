# Generated by Django 5.0.4 on 2024-05-08 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_choice_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='date_added',
            new_name='created_at',
        ),
    ]
