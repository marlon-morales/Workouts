# Generated by Django 3.1.7 on 2021-09-18 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id_area', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Ejercicios',
            fields=[
                ('id_ejercicios', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=150)),
                ('duracion', models.IntegerField()),
                ('explicacion', models.CharField(max_length=150)),
                ('link_entreno', models.CharField(max_length=150)),
                ('id_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkoutsApp.areas')),
            ],
        ),
        migrations.CreateModel(
            name='Planes',
            fields=[
                ('id_plan', models.AutoField(primary_key=True, serialize=False)),
                ('dias_disponibles', models.IntegerField()),
                ('dias_entrenados', models.IntegerField()),
                ('dias_esta_semana', models.IntegerField()),
                ('num_sesiones', models.IntegerField()),
                ('ultima_semana', models.DateField()),
                ('id_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkoutsApp.areas')),
            ],
        ),
        migrations.CreateModel(
            name='Rangos',
            fields=[
                ('id_rango', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('edad', models.IntegerField()),
                ('peso', models.CharField(max_length=4)),
                ('estatura', models.CharField(max_length=4)),
                ('ciudad', models.CharField(max_length=50)),
                ('puntaje_habilidades', models.IntegerField()),
                ('fk_user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_rango', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkoutsApp.rangos')),
            ],
        ),
        migrations.CreateModel(
            name='Sesiones',
            fields=[
                ('id_sesion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('num_sesiones', models.IntegerField()),
                ('id_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkoutsApp.planes')),
            ],
        ),
        migrations.CreateModel(
            name='Sesion_Ejercicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_ejercicios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkoutsApp.ejercicios')),
                ('id_sesion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkoutsApp.sesiones')),
            ],
        ),
        migrations.AddField(
            model_name='planes',
            name='id_rango',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkoutsApp.rangos'),
        ),
        migrations.AddField(
            model_name='planes',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkoutsApp.usuarios'),
        ),
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id_habilidades', models.AutoField(primary_key=True, serialize=False)),
                ('flexibilidad', models.IntegerField()),
                ('fuerza', models.IntegerField()),
                ('resistencia', models.IntegerField()),
                ('velocidad', models.IntegerField()),
                ('aceleracion', models.IntegerField()),
                ('agilidad', models.IntegerField()),
                ('coordinacion', models.IntegerField()),
                ('precision', models.IntegerField()),
                ('fk_user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_rango', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkoutsApp.rangos')),
            ],
        ),
        migrations.AddField(
            model_name='ejercicios',
            name='id_rango',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkoutsApp.rangos'),
        ),
    ]