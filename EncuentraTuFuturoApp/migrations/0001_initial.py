# Generated by Django 4.2.7 on 2023-11-19 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='administrador',
            fields=[
                ('idAdministrador', models.AutoField(primary_key=True, serialize=False)),
                ('Nombreadm', models.CharField(max_length=30)),
                ('Apellidoadm', models.CharField(max_length=30)),
                ('correoadm', models.CharField(max_length=30)),
                ('Contraseñaadm', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('idcarrera', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=30)),
                ('Arancel', models.PositiveIntegerField(blank=True, null=True)),
                ('Duracion', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('idinstitucion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=25)),
                ('informacion', models.CharField(max_length=50)),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=30)),
                ('Apellido', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
                ('Contraseña', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('idfavorito', models.AutoField(primary_key=True, serialize=False)),
                ('IdCarrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EncuentraTuFuturoApp.carrera')),
                ('IdUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EncuentraTuFuturoApp.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='carrera',
            name='idinstitucion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EncuentraTuFuturoApp.institucion'),
        ),
    ]