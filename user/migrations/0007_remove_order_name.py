# Generated by Django 3.1.2 on 2020-10-26 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20201024_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
    ]
