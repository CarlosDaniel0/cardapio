# Generated by Django 3.1.5 on 2021-01-13 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='documents/')),
                ('nome', models.CharField(max_length=200)),
                ('valor', models.FloatField()),
            ],
        ),
    ]
