# Generated by Django 3.2.5 on 2021-07-23 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addpeople', '0008_alter_person_createdby'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
