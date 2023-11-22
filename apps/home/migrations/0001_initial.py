# Generated by Django 3.2.16 on 2023-11-01 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('nationality', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Plataform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('icon', models.ImageField(upload_to='icons/')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('gender', models.CharField(max_length=50)),
                ('duration', models.IntegerField()),
                ('cover', models.ImageField(upload_to='covers/')),
                ('year', models.DateField()),
                ('ranking', models.IntegerField()),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='get_directors', to='home.director')),
                ('plataform', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='get_plataformas', to='home.plataform')),
            ],
        ),
    ]
