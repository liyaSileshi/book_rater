# Generated by Django 2.2.6 on 2019-12-07 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rater', '0008_auto_20191207_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.CharField(default='book image url', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='book title', max_length=200, null=True),
        ),
    ]
