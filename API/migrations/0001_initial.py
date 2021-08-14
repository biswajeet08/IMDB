# Generated by Django 3.2.6 on 2021-08-12 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IMDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popularity', models.FloatField(db_column='99popularity')),
                ('director', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=100)),
                ('imdb_score', models.FloatField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
