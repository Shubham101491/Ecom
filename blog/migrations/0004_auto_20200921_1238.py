# Generated by Django 2.2.10 on 2020-09-21 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200921_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=50)),
                ('blog_images', models.ImageField(upload_to='blog/')),
                ('blog_content', models.CharField(max_length=500)),
                ('blog_date', models.DateField()),
            ],
        ),
        migrations.RenameField(
            model_name='blog_category',
            old_name='category',
            new_name='blog_category',
        ),
        migrations.DeleteModel(
            name='Blogs',
        ),
        migrations.AddField(
            model_name='blog_data',
            name='blog_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog_Category'),
        ),
    ]
