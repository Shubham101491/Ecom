# Generated by Django 2.2.10 on 2020-10-06 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
    ]
