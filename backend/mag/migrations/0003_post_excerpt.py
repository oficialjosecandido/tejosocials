# Generated by Django 3.0.7 on 2021-11-22 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mag', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
