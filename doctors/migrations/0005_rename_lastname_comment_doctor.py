# Generated by Django 4.0.2 on 2023-06-24 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0004_rename_doctor_comment_lastname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='lastname',
            new_name='doctor',
        ),
    ]
