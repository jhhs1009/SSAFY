# Generated by Django 3.2.13 on 2023-04-14 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movie_like_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='movie_id',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='user_id',
            new_name='user',
        ),
    ]
