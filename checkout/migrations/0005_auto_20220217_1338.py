# Generated by Django 3.0.14 on 2022-02-17 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_alter_shipping_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]