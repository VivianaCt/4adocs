# Generated by Django 3.2.7 on 2021-11-23 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_alter_stock_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telefono',
            field=models.CharField(max_length=10, verbose_name='Telefono'),
        ),
    ]
