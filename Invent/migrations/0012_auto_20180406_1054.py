# Generated by Django 2.0.3 on 2018-04-06 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invent', '0011_auto_20180406_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='Account',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
