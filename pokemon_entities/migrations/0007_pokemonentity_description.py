# Generated by Django 3.1.14 on 2022-02-17 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0006_auto_20220216_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
