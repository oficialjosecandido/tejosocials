# Generated by Django 3.0.7 on 2021-12-12 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mag', '0005_post_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='type',
            new_name='tag',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='post',
            name='small_image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
    ]
