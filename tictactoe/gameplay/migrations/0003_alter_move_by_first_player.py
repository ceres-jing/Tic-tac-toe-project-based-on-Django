# Generated by Django 4.2.8 on 2023-12-12 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gameplay", "0002_game_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="move",
            name="by_first_player",
            field=models.BooleanField(editable=False),
        ),
    ]
