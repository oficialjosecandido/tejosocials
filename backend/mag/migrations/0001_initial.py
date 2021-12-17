# Generated by Django 3.0.7 on 2021-11-20 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contactId', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateField(auto_now_add=True)),
                ('senderName', models.CharField(blank=True, max_length=100, null=True)),
                ('senderEmail', models.CharField(blank=True, max_length=100, null=True)),
                ('senderMessage', models.TextField(blank=True, null=True)),
                ('senderSKU', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Unread', 'Unread')], max_length=64)),
            ],
        ),
    ]
