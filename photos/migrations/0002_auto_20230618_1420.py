# Generated by Django 3.2.19 on 2023-06-18 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='photos',
            options={'verbose_name_plural': 'Photos'},
        ),
    ]
