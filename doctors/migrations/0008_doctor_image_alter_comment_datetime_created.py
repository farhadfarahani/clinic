# Generated by Django 4.0.2 on 2023-07-05 19:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0007_alter_comment_author_alter_comment_body_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime_created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date time of creation'),
        ),
    ]