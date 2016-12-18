# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('account', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=15)),
                ('image', models.ImageField(upload_to='')),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('kind', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('on_sale', models.BooleanField()),
                ('publish_time', models.DateTimeField()),
                ('score', models.IntegerField(default=0)),
                ('publisher', models.ForeignKey(to='rango.MyUser')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(to='rango.Product'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='rango.MyUser'),
        ),
    ]
