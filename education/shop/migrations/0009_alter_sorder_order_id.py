# Generated by Django 5.0.2 on 2024-04-14 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_sorder_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorder',
            name='order_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
