# Generated by Django 4.2.4 on 2023-11-08 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('user_type', models.CharField(choices=[('user', 'User'), ('admin', 'Admin'), ('super_admin', 'Super Admin'), ('partner', 'Partner')], default='user', max_length=255)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_logo', models.ImageField(upload_to='company_logo')),
                ('company_name', models.CharField(max_length=255)),
                ('company_address', models.CharField(max_length=255)),
                ('company_email', models.EmailField(max_length=255)),
                ('company_phone', models.CharField(max_length=255)),
                ('company_website', models.CharField(max_length=255)),
                ('company_facebook', models.CharField(max_length=255)),
                ('company_twitter', models.CharField(max_length=255)),
                ('company_instagram', models.CharField(max_length=255)),
                ('company_text_color', models.CharField(default='#ffffff', max_length=255)),
                ('company_primary_color', models.CharField(default='#ffffff', max_length=255)),
                ('company_secondary_color', models.CharField(default='#ffffff', max_length=255)),
                ('company_copyright', models.CharField(default='Beyonderissolutions', max_length=255)),
                ('company_button_color', models.CharField(default='#ffffff', max_length=255)),
                ('company_starting_year', models.CharField(default='2021', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ForgetPassword',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='forget_password', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('reset_email_token', models.CharField(max_length=255)),
                ('activated', models.BooleanField(default=True)),
                ('is_expired', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'ForgetPassword',
            },
        ),
        migrations.CreateModel(
            name='UserActivation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('otp', models.CharField(blank=True, max_length=50, null=True)),
                ('activated', models.BooleanField(default=False)),
                ('is_expired', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_activation', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'UserActivation',
            },
        ),
    ]
