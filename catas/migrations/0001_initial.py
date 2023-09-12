# Generated by Django 3.0.5 on 2023-09-11 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('digital', models.BooleanField(blank=True, default=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('date', models.DateTimeField(blank=True)),
                ('duration', models.CharField(max_length=50)),
            ],
        ),
    ]
