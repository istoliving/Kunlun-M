# Generated by Django 3.0.7 on 2020-08-17 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_scanresulttask_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scanresulttask',
            name='rule_id',
        ),
    ]
