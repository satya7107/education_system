# Generated by Django 5.0.2 on 2024-04-14 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_order_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorder',
            name='order_id',
            field=models.IntegerField(default='', primary_key=True, serialize=False),
        ),
    ]