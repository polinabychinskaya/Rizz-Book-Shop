# Generated by Django 4.2.1 on 2023-06-12 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0007_alter_title_genre_alter_title_publishing_house'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='picture',
            field=models.ImageField(default='-', upload_to='uploads/%Y/%m/%d/', verbose_name='Book picture'),
            preserve_default=False,
        ),
    ]
