# Generated by Django 3.2.5 on 2021-07-23 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addpeople', '0012_auto_20210723_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
