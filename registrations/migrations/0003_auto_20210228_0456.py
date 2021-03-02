# Generated by Django 3.1.6 on 2021-02-27 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0002_auto_20210221_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managerregistrationtable',
            name='Restaurant_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrations.restaurantregistrationtable'),
        ),
        migrations.AlterField(
            model_name='staffregistrationtable',
            name='Restaurant_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registrations.restaurantregistrationtable'),
        ),
    ]