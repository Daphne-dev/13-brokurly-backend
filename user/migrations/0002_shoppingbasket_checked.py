# Generated by Django 3.1.2 on 2020-10-23 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingbasket',
            name='checked',
            field=models.BooleanField(default=True),
        ),
    ]
