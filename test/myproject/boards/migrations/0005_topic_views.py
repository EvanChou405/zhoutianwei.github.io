# Generated by Django 2.2 on 2019-07-24 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]