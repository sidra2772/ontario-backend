# Generated by Django 3.2.15 on 2024-04-29 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_services_service_slug'),
        ('notification', '0003_alter_notificationdetails_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationdetails',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_notification', to='services.services'),
        ),
    ]
