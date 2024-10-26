# Generated by Django 3.2.15 on 2024-05-20 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FooterForCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_heading', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Footer For Categories',
                'verbose_name_plural': 'Footer For Categories',
            },
        ),
        migrations.CreateModel(
            name='HeaderforCategoriesPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_heading', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.FileField(upload_to='categories_page_header/')),
            ],
            options={
                'verbose_name': 'Header for Categories Page',
                'verbose_name_plural': 'Header for Categories Page',
            },
        ),
    ]