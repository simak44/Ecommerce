# Generated by Django 5.0.1 on 2024-03-29 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_reviewmodel_titleproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartmodel',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='productshortdescriptionmodel',
            name='description',
            field=models.TextField(default=None),
        ),
    ]