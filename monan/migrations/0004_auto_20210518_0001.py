# Generated by Django 3.1.7 on 2021-05-17 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monan', '0003_post_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
