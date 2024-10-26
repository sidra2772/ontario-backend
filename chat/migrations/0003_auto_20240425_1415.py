# Generated by Django 3.2.15 on 2024-04-25 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_rename_services_orders_service'),
        ('chat', '0002_onlineuser_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommessage',
            name='is_custom_order',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='roommessage',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_room_messages', to='dashboard.orders'),
        ),
    ]