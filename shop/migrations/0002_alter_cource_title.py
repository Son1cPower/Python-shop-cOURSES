# Generated by Django 4.0.8 on 2023-02-20 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cource',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
