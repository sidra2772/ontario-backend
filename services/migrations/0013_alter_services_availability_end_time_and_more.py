# Generated by Django 5.0.6 on 2024-11-13 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0012_services_discounted_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='availability_end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='availability_start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]