# Generated by Django 3.0.14 on 2022-02-04 11:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_auto_20220204_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='reward_point',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(3), django.core.validators.MinValueValidator(0)]),
        ),
    ]