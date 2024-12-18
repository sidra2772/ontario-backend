# Generated by Django 3.2.15 on 2024-04-19 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_callingcodewithname_currency'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='currency',
            unique_together={('name', 'code')},
        ),
        migrations.RemoveField(
            model_name='currency',
            name='exchange_rate',
        ),
        migrations.RemoveField(
            model_name='currency',
            name='symbol',
        ),
    ]
