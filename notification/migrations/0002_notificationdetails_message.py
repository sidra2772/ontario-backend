# Generated by Django 3.2.15 on 2024-04-15 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationdetails',
            name='message',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]