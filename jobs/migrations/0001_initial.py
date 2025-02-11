# Generated by Django 5.0.6 on 2024-12-30 15:41

import django.contrib.postgres.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0015_alter_businessprofile_business_domain_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, null=True, size=None)),
                ('bid_closing_date', models.DateTimeField()),
                ('duration_in_months', models.PositiveIntegerField()),
                ('submission_type', models.CharField(max_length=255)),
                ('condition_for_participation', models.TextField()),
                ('agreement', models.FileField(blank=True, null=True, upload_to='jobs/agreements/')),
            ],
            options={
                'verbose_name_plural': 'Jobs',
                'db_table': 'jobs',
            },
        ),
        migrations.CreateModel(
            name='JobBids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bid_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bid_description', models.TextField()),
                ('due_date', models.DateTimeField()),
                ('cover_letter', models.TextField()),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='userprofile.userprofile')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='jobs.jobs')),
            ],
            options={
                'verbose_name_plural': 'Job Bids',
                'db_table': 'job_bids',
            },
        ),
    ]
