# Generated by Django 4.2.7 on 2023-12-26 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('cancelled', 'cancelled'), ('delivered', 'delivered'), ('shipped', 'shipped'), ('pending', 'pending')], default='pending', max_length=50),
        ),
    ]
