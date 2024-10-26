# Generated by Django 3.2.15 on 2024-04-26 10:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0007_userprofile_zip_code'),
        ('dashboard', '0002_rename_services_orders_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('report_number', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Report Number')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('subject', models.CharField(choices=[('other', 'Other'), ('bug', 'Bug'), ('feature', 'Feature'), ('question', 'Question'), ('suggestion', 'Suggestion'), ('complaint', 'Complaint'), ('order_report', 'Order Report')], default='other', max_length=50)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('closed', 'Closed'), ('pending', 'Pending'), ('resolved', 'Resolved'), ('in_progress', 'In Progress')], default='pending', max_length=50)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_reports', to='dashboard.orders')),
                ('receiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver_reports', to='userprofile.userprofile')),
                ('reporter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_reports', to='userprofile.userprofile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReportImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='reports/')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_images', to='helpandsupport.report')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
