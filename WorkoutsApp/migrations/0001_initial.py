# Generated by Django 3.1.7 on 2021-03-20 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_area', models.IntegerField()),
                ('descripcion', models.CharField(max_length=150)),
                ('links', models.CharField(max_length=150)),
                ('sesiones', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ejercicios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_ejercicios', models.IntegerField()),
                ('descripcion', models.CharField(max_length=150)),
                ('duracion', models.IntegerField()),
                ('explicacion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Rangos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_habilidad', models.IntegerField()),
                ('nivel_habilidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('peso', models.CharField(max_length=3)),
                ('estatura', models.CharField(max_length=3)),
                ('correo', models.EmailField(max_length=254)),
                ('contra', models.CharField(max_length=15)),
                ('ciudad', models.CharField(max_length=50)),
                ('puntajehabilidad', models.IntegerField()),
                ('id_habilidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkoutsApp.rangos')),
            ],
        ),
        migrations.CreateModel(
            name='Planes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_plan', models.IntegerField()),
                ('diasdisponibles', models.IntegerField()),
                ('diasentrenados', models.IntegerField()),
                ('dias_esta_semana', models.IntegerField()),
                ('id_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkoutsApp.areas')),
                ('id_ejercicios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkoutsApp.ejercicios')),
                ('id_habilidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkoutsApp.rangos')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkoutsApp.usuarios')),
            ],
        ),
        migrations.AddField(
            model_name='ejercicios',
            name='id_habilidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WorkoutsApp.rangos'),
        ),
    ]
