# Generated by Django 5.0.6 on 2024-08-15 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_services_attachment_services_short_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
