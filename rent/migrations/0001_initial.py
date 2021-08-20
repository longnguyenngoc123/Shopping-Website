# Generated by Django 3.1.7 on 2021-05-18 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('date', models.DateTimeField(blank=True)),
                ('address', models.TextField(null=True)),
                ('level', models.IntegerField(null=True)),
                ('phone', models.IntegerField(null=True)),
            ],
        ),
    ]