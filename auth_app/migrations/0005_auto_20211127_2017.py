# Generated by Django 3.2.7 on 2021-11-28 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0004_user_superuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='sku',
        ),
        migrations.AlterField(
            model_name='stock',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]