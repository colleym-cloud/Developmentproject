# Generated by Django 4.2.10 on 2024-02-14 11:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ffinderapp", "0002_remove_player_age_player_address_player_city_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True),
        ),
    ]
