# Generated by Django 4.0.3 on 2023-02-19 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('humidity', models.IntegerField()),
                ('temprature', models.IntegerField()),
                ('rosa', models.IntegerField()),
                ('wind_speed', models.IntegerField()),
                ('pressure', models.IntegerField()),
                ('feels_like', models.IntegerField()),
                ('uv_index', models.IntegerField()),
                ('pollution', models.IntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weather', to='pogooda.city')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weather', to='pogooda.day')),
            ],
        ),
    ]
