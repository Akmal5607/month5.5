# Generated by Django 4.2.2 on 2023-06-24 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.IntegerField(choices=[[1, '*'], [2, '**'], [3, '***'], [4, '****'], [5, '*****']], default=0),
        ),
    ]
