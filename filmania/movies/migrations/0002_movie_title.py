# Generated by Django 4.0 on 2022-01-11 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
