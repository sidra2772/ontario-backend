# Generated by Django 3.2.15 on 2024-06-04 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpandsupport', '0004_report_email'),
        ('chat', '0009_alter_room_dispute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='dispute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dispute_rooms', to='helpandsupport.report'),
        ),
    ]
