# Generated by Django 3.0.5 on 2023-09-12 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20230912_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='crianza',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='grape_variety',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='producer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
