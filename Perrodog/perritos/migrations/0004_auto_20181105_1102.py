# Generated by Django 2.1.2 on 2018-11-05 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perritos', '0003_auto_20181024_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nuevo',
            name='foto',
            field=models.ImageField(upload_to='media'),
        ),
    ]