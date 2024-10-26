# Generated by Django 5.0.6 on 2024-06-10 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0011_remove_businessprofile_user_profile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessprofile',
            name='business_description',
        ),
        migrations.RemoveField(
            model_name='businessprofile',
            name='business_email',
        ),
        migrations.RemoveField(
            model_name='businessprofile',
            name='business_image',
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='business_domain',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='business_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='account_type',
            field=models.CharField(choices=[('business_member', 'Business Member'), ('individual', 'Individual'), ('business_admin', 'Business Admin')], default='individual', max_length=255),
        ),
    ]