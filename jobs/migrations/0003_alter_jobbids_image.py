# Generated by Django 5.0.6 on 2025-03-18 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_jobs_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobbids',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='jobs/bids/'),
        ),
    ]
