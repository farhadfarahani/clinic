# Generated by Django 4.0.2 on 2023-06-24 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='doctor',
            new_name='lastname',
        ),
    ]
