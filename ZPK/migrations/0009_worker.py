# Generated by Django 2.0.3 on 2018-04-03 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZPK', '0008_auto_20180328_0813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LastName', models.CharField(max_length=200)),
                ('FirstName', models.CharField(max_length=200)),
                ('Age', models.DateField()),
                ('Sallary', models.IntegerField(max_length=100)),
            ],
        ),
    ]
