# Generated by Django 3.2.15 on 2024-05-31 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpandsupport', '0003_auto_20240429_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
