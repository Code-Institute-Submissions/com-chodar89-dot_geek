# Generated by Django 3.0 on 2019-12-05 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexcarousel',
            name='image',
            field=models.ImageField(upload_to='photos/carousel/%Y/%m/%d'),
        ),
    ]