# Generated by Django 5.0.6 on 2024-08-06 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category_blogpost_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='BlogCategory',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='category',
            new_name='blog_category',
        ),
    ]