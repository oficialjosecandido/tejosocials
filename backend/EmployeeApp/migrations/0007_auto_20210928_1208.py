# Generated by Django 3.0.7 on 2021-09-28 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0006_techreport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='techreport',
            name='EmployeeName',
        ),
        migrations.AlterField(
            model_name='techreport',
            name='techCompany',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='techreport',
            name='techVAT',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
