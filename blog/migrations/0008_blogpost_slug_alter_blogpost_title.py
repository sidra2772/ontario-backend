# Generated by Django 5.0.6 on 2025-01-12 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_blogpost_slug_blogpost_short_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default=1, editable=False, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
