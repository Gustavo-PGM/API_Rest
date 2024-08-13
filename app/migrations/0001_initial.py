# Generated by Django 5.1 on 2024-08-12 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('apelido', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('idade', models.IntegerField()),
            ],
        ),
    ]
