# Generated by Django 3.1.6 on 2021-04-05 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POS', '0002_auto_20210405_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermanagementtable',
            name='Customer_Phone',
            field=models.BigIntegerField(),
        ),
    ]
