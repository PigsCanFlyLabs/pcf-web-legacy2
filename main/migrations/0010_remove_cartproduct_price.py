# Generated by Django 3.2.14 on 2022-12-21 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_product_external_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartproduct',
            name='price',
        ),
    ]