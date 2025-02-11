# Generated by Django 3.2.15 on 2024-05-23 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20240520_1213'),
        ('notification', '0004_notificationdetails_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationdetails',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_notification', to='dashboard.orders'),
        ),
    ]
