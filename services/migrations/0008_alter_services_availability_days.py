# Generated by Django 3.2.15 on 2024-06-03 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_auto_20240603_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='availability_days',
            field=models.CharField(choices=[('all_days', 'All Days'), ('week_days', 'Week Days'), ('weekend', 'Weekend')], default='all_days', max_length=255),
        ),
    ]
