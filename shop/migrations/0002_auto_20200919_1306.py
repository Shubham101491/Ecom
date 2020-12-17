# Generated by Django 2.2.10 on 2020-09-19 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watch_title', models.CharField(max_length=50)),
                ('watch_pic', models.ImageField(upload_to='watches/')),
                ('watch_detail', models.CharField(max_length=200)),
                ('watch_price', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Watches',
        ),
    ]
