# Generated by Django 3.2.15 on 2024-04-24 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0003_alter_services_currency'),
        ('userprofile', '0007_userprofile_zip_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_custom_offer', models.BooleanField(default=False)),
                ('payment_via', models.CharField(blank=True, choices=[('paypal', 'Paypal'), ('stripe', 'Stripe')], max_length=255, null=True)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('canceled', 'Canceled'), ('rejected', 'Rejected'), ('completed', 'Completed'), ('refunded', 'Refunded'), ('in_progress', 'in_progress'), ('in_revision', 'In Revision'), ('withdraw', 'Withdraw')], default='pending', max_length=25)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_number', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('hiring_date', models.DateTimeField(blank=True, null=True)),
                ('is_payment', models.BooleanField(default=False)),
                ('service_fee', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_offer', to='userprofile.userprofile')),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_offer', to='services.services')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
