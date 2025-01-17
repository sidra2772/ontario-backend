# Generated by Django 3.2.15 on 2024-06-04 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0009_alter_userprofile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='account_type',
            field=models.CharField(choices=[('business', 'Business'), ('individual', 'Individual'), ('admin', 'Admin')], default='individual', max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='BusinessProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('business_name', models.CharField(max_length=255)),
                ('business_email', models.EmailField(max_length=254)),
                ('business_domain', models.CharField(max_length=255)),
                ('business_description', models.TextField()),
                ('business_image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='business_profile', to='userprofile.userprofile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
