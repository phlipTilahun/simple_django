# Generated by Django 3.2.5 on 2021-07-23 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addpeople', '0009_alter_person_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='createdBy',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
