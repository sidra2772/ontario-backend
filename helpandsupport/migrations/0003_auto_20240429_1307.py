# Generated by Django 3.2.15 on 2024-04-29 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpandsupport', '0002_auto_20240429_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
