# Generated by Django 3.1.7 on 2021-05-26 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monan', '0007_auto_20210526_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='../media/'),
        ),
    ]
