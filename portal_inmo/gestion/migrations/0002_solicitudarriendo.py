# Generated by Django 5.0.6 on 2024-07-02 02:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gestion", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SolicitudArriendo",
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
                ("mensaje", models.TextField()),
                ("fecha_solicitud", models.DateTimeField(auto_now_add=True)),
                ("estado", models.CharField(default="pendiente", max_length=20)),
                (
                    "arrendatario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "propiedad",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gestion.propiedad",
                    ),
                ),
            ],
        ),
    ]
