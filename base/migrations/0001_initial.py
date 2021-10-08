# Generated by Django 3.2.8 on 2021-10-08 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.TextField()),
                ('disponivel', models.BooleanField(default=False)),
                ('alternativas', models.JSONField()),
                ('alternativa', models.IntegerField(choices=[(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D')])),
            ],
        ),
    ]
