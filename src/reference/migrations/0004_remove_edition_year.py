# Generated by Django 4.2.1 on 2023-05-20 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0003_title_edition_title_genre_title_publishing_house'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edition',
            name='year',
        ),
    ]