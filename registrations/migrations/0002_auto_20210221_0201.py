# Generated by Django 3.1.6 on 2021-02-20 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact',
            field=models.BigIntegerField(),
        ),
    ]
