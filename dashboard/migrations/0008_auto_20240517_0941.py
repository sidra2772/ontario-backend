# Generated by Django 3.2.15 on 2024-05-17 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_rename_is_service_fee_orders_is_paid_service_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='cancel_reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('canceled', 'Canceled'), ('rejected', 'Rejected'), ('completed', 'Completed'), ('refunded', 'Refunded'), ('in_progress', 'in_progress'), ('in_revision', 'In Revision'), ('withdraw', 'Withdraw')], default='in_progress', max_length=25),
        ),
    ]
