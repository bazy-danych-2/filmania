# Generated by Django 4.0 on 2022-01-11 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='short_desc',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='model_img',
            field=models.ImageField(upload_to='movies_photos'),
        ),
    ]
