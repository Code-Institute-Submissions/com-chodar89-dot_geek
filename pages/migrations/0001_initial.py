# Generated by Django 3.0 on 2019-12-05 21:11

from django.db import migrations, models
import exclusivebooleanfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndexCarousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/carousel')),
                ('heading', models.CharField(blank=True, max_length=150)),
                ('paragraph', models.CharField(blank=True, max_length=300)),
                ('first', exclusivebooleanfield.fields.ExclusiveBooleanField()),
            ],
        ),
    ]
