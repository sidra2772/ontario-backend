# Generated by Django 5.0.6 on 2025-01-02 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_jobs_user_alter_jobbids_bidder'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobbids',
            name='bit_type',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
