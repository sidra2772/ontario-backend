# Generated by Django 3.2.15 on 2024-04-29 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_grouproommessage_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouproom',
            name='group_type',
            field=models.CharField(choices=[('group', 'Group'), ('report', 'Report')], default='group', max_length=255),
        ),
    ]
