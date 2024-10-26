# Generated by Django 3.2.15 on 2024-04-19 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('index', models.PositiveBigIntegerField(default=0)),
                ('name', models.CharField(error_messages={'unique': 'This Category has already been registered.'}, max_length=100, unique=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('common_name', models.CharField(max_length=255)),
                ('official_name', models.CharField(blank=True, max_length=255, null=True)),
                ('alpha_code_2', models.CharField(blank=True, max_length=10, null=True)),
                ('alpha_code_3', models.CharField(blank=True, max_length=10, null=True)),
                ('flag_png', models.CharField(blank=True, max_length=255, null=True)),
                ('flag_svg', models.CharField(blank=True, max_length=255, null=True)),
                ('flag_png_file', models.FileField(blank=True, max_length=255, null=True, upload_to='')),
                ('flag_svg_file', models.FileField(blank=True, max_length=255, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Countries',
                'db_table': 'countries',
            },
        ),
        migrations.CreateModel(
            name='CountryTimeZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('timezone', models.CharField(max_length=255)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='timezones', to='assets.countries')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('image', models.FileField(blank=True, null=True, upload_to='subcategory')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='assets.categories')),
            ],
            options={
                'verbose_name_plural': 'Sub Categories',
                'db_table': 'sub_categories',
                'unique_together': {('category', 'name')},
            },
        ),
    ]