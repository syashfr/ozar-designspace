# Generated by Django 3.1.1 on 2021-03-16 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designspace', '0003_design_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
