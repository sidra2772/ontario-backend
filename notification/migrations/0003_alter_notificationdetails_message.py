# Generated by Django 3.2.15 on 2024-04-29 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_grouproom_group_type'),
        ('notification', '0002_notificationdetails_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationdetails',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message_notification', to='chat.roommessage'),
        ),
    ]
