# Generated by Django 2.0.3 on 2018-04-17 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ship',
            name='Photo',
            field=models.ImageField(blank=True, height_field=300, null=True, upload_to='ships', width_field=750),
        ),
    ]
