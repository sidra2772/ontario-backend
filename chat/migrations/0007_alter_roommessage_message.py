# Generated by Django 3.2.15 on 2024-05-28 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_grouproom_group_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roommessage',
            name='message',
            field=models.TextField(blank=True, max_length=90000, null=True),
        ),
    ]
