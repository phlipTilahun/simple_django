# Generated by Django 3.2.5 on 2021-07-23 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addpeople', '0013_alter_person_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]
