# Generated by Django 3.1.3 on 2020-11-18 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0004_cur_lastupdated'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompareOutput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField()),
                ('name', models.CharField(max_length=50)),
                ('link', models.URLField()),
            ],
        ),
    ]
