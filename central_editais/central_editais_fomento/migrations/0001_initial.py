# Generated by Django 3.0.4 on 2020-03-10 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('resumo', models.CharField(max_length=1000)),
                ('texto', models.TextField()),
                ('data_limite', models.DateField()),
                ('areas', models.CharField(max_length=1000)),
                ('tipos', models.CharField(max_length=1000)),
            ],
        ),
    ]
