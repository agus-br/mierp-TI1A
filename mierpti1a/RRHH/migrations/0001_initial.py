# Generated by Django 4.2.16 on 2024-10-07 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Empleado",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=100)),
                ("apellidos", models.CharField(max_length=100)),
                ("numero", models.CharField(max_length=15)),
                ("fecha_nac", models.DateField(verbose_name="Fecha de nacimiento")),
                (
                    "estado_civil",
                    models.CharField(
                        choices=[
                            ("S", "Soltero/a"),
                            ("C", "Casado/a"),
                            ("D", "Divorciado/a"),
                            ("V", "Viudo/a"),
                        ],
                        max_length=1,
                    ),
                ),
                ("edad", models.IntegerField()),
                ("correo", models.EmailField(max_length=254)),
                (
                    "sexo",
                    models.CharField(
                        choices=[("M", "Masculino"), ("F", "Femenino"), ("O", "Otro")],
                        max_length=1,
                    ),
                ),
                ("rfc", models.CharField(max_length=13)),
                ("curp", models.CharField(max_length=18)),
                ("departamento", models.CharField(max_length=100)),
                ("puesto", models.CharField(max_length=100)),
            ],
        ),
    ]