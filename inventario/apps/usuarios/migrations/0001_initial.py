# Generated by Django 2.0.2 on 2018-03-06 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombre', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('departamento', models.CharField(blank=True, max_length=40)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('fuera_convenio', models.CharField(max_length=5)),
            ],
        ),
    ]
