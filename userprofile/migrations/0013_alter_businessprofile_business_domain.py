# Generated by Django 5.0.6 on 2024-06-11 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0012_remove_businessprofile_business_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessprofile',
            name='business_domain',
            field=models.URLField(max_length=255, unique=True),
        ),
    ]