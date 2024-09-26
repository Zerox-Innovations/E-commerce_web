# Generated by Django 5.1 on 2024-09-11 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userside', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='delivery_charge',
            field=models.IntegerField(default=40),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('UPI', 'UPI'), ('COD', 'Cash on delivary')], max_length=50),
        ),
    ]
