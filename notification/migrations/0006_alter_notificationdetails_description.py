# Generated by Django 3.2.15 on 2024-05-29 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0005_notificationdetails_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationdetails',
            name='description',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
    ]