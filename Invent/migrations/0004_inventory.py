# Generated by Django 2.0.3 on 2018-04-05 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Invent', '0003_delete_inventory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Account', models.IntegerField()),
                ('Lifetime', models.IntegerField()),
                ('Comissioning', models.DateField()),
                ('MOL', models.CharField(max_length=200)),
                ('InvNum', models.IntegerField()),
                ('FactoryNum', models.IntegerField()),
                ('Location', models.CharField(max_length=200)),
            ],
        ),
    ]