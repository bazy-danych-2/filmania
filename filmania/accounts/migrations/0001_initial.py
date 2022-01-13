# Generated by Django 4.0 on 2022-01-12 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('movies', '0004_remove_movie_reated'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ulubione_filmy', models.ManyToManyField(to='movies.Movie')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]