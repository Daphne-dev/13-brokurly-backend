# Generated by Django 3.1.2 on 2020-10-27 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20201023_1336'),
        ('user', '0013_auto_20201027_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingbasket',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productoption'),
        ),
    ]
