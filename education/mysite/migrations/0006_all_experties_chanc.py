# Generated by Django 5.0.2 on 2024-02-26 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_all_experties_ceo'),
    ]

    operations = [
        migrations.CreateModel(
            name='all_experties_chanc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=20, unique=True)),
                ('image', models.ImageField(upload_to='images')),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]
