# Generated by Django 2.2.7 on 2020-01-28 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0003_databaseinformation_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='databaseinformation',
            name='img',
        ),
    ]
