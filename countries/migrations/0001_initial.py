# Generated by Django 5.2 on 2025-05-05 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Language",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=10, unique=True)),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("cca2", models.CharField(max_length=2, unique=True)),
                ("capital", models.CharField(blank=True, max_length=100, null=True)),
                ("population", models.BigIntegerField()),
                ("region", models.CharField(max_length=100)),
                ("timezones", models.JSONField()),
                ("flag", models.URLField()),
                ("languages", models.ManyToManyField(to="countries.language")),
            ],
        ),
    ]
