# Generated by Django 4.1 on 2022-09-04 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='news/'),
        ),
    ]