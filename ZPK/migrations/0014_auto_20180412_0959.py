# Generated by Django 2.0.3 on 2018-04-12 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZPK', '0013_phonebook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonebook',
            name='FirstName',
        ),
        migrations.RemoveField(
            model_name='phonebook',
            name='LastName',
        ),
        migrations.AddField(
            model_name='phonebook',
            name='FIO',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
