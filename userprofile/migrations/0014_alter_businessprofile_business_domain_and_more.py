# Generated by Django 5.0.6 on 2024-07-30 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0013_alter_businessprofile_business_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessprofile',
            name='business_domain',
            field=models.URLField(max_length=255),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='business_name',
            field=models.CharField(max_length=255),
        ),
    ]