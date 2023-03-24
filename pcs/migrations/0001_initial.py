# Generated by Django 3.1.3 on 2023-03-24 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu', models.TextField(blank=True)),
                ('gpu', models.TextField(blank=True)),
                ('ram', models.TextField(blank=True)),
                ('mobo', models.TextField(blank=True)),
                ('psu', models.TextField(blank=True)),
                ('data', models.TextField(blank=True)),
                ('gabo', models.TextField(blank=True)),
                ('monitor', models.TextField(blank=True)),
                ('teclado', models.TextField(blank=True)),
                ('mouse', models.TextField(blank=True)),
            ],
        ),
    ]
