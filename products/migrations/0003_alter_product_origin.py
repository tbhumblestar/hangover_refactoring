# Generated by Django 4.0.6 on 2022-07-16 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_explanation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='origin',
            field=models.CharField(max_length=100),
        ),
    ]