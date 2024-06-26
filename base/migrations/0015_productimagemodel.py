# Generated by Django 5.0.1 on 2024-04-17 05:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_cartmodel_quantity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productimage', models.ImageField(upload_to='productimg')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.productmodel')),
            ],
        ),
    ]
