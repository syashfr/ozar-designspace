# Generated by Django 3.1.1 on 2020-10-23 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0005_auto_20201008_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='name',
        ),
    ]
