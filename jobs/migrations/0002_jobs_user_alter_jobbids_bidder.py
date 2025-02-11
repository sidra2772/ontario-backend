# Generated by Django 5.0.6 on 2024-12-30 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
        ('userprofile', '0015_alter_businessprofile_business_domain_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='userprofile.userprofile'),
        ),
        migrations.AlterField(
            model_name='jobbids',
            name='bidder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='userprofile.userprofile'),
        ),
    ]
