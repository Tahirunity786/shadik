# Generated by Django 5.0.4 on 2024-04-24 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_cart_id_alter_customer_id_alter_customer_state_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplaced',
            name='user',
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='app.customer'),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='app.product'),
        ),
    ]