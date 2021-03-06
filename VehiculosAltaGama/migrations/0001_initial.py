# Generated by Django 4.0.5 on 2022-06-28 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camioneta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=20)),
                ('anio', models.IntegerField()),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Deportivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=20)),
                ('anio', models.IntegerField()),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sedan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('modelo', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=20)),
                ('anio', models.IntegerField()),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
