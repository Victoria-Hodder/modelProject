# Generated by Django 3.0.3 on 2020-02-28 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='simple',
            name='number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='simple',
            name='url',
            field=models.URLField(default='www.example.com'),
        ),
    ]
