# Generated by Django 3.2.5 on 2021-07-23 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addpeople', '0010_alter_person_createdby'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=6)),
                ('createdBy', models.IntegerField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='createdBy',
        ),
    ]
