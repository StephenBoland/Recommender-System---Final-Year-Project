# Generated by Django 2.2.7 on 2020-02-08 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0014_auto_20200208_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breweryinformation',
            name='img',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='databaseinformation',
            name='img',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
