# Generated by Django 3.1.7 on 2021-05-30 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210530_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default='NoName', max_length=30),
        ),
    ]