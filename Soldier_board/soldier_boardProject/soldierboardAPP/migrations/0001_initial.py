# Generated by Django 5.0.2 on 2024-02-19 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esm_no', models.IntegerField()),
                ('esm_name', models.CharField(max_length=30)),
                ('resident', models.CharField(max_length=20)),
                ('service_no', models.IntegerField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
