# Generated by Django 2.0.3 on 2018-03-16 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ZPK', '0003_auto_20180315_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otdel',
            name='sotrudnik',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ZPK.Person'),
        ),
    ]
