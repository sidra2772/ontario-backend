# Generated by Django 3.2.15 on 2023-11-09 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_user_phone_number_alter_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivation',
            name='otp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
