# Generated by Django 5.1.2 on 2024-10-29 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id_sucursal', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('id_empleado', models.CharField(max_length=10)),
                ('horario', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=50)),
            ],
        ),
    ]
