# Generated by Django 4.1.1 on 2022-09-11 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TrainingResult",
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
                ("type", models.CharField(max_length=32)),
                ("filename", models.CharField(max_length=64)),
                ("time", models.CharField(max_length=64)),
                ("auc", models.CharField(max_length=64)),
                ("macro", models.CharField(max_length=64)),
                ("macro_recall", models.CharField(max_length=64)),
                ("weighted", models.CharField(max_length=64)),
                ("result_url", models.CharField(max_length=128)),
            ],
        ),
    ]
