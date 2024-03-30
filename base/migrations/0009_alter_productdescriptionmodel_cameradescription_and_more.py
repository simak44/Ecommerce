# Generated by Django 5.0.1 on 2024-03-26 05:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_remove_productdescriptionmodel_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdescriptionmodel',
            name='cameradescription',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='productdescriptionmodel',
            name='designdescription',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='productdescriptionmodel',
            name='technologydescription',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='productdescriptionmodel',
            name='titledescription',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='productdescriptionmodel',
            name='touchdescription',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.CreateModel(
            name='ProductShortDescriptionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('productname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.productmodel')),
            ],
        ),
    ]