# Generated by Django 3.2.14 on 2022-12-27 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_cartproduct_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproduct',
            name='cart',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.cart'),
            preserve_default=False,
        ),
    ]
