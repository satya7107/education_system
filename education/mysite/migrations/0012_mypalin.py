# Generated by Django 5.0.2 on 2024-04-25 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_main_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='mypalin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myname', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
