# Generated by Django 2.2.7 on 2020-01-28 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0006_auto_20200128_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='databaseinformation',
            name='abv',
            field=models.DecimalField(decimal_places=2, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='databaseinformation',
            name='description',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='databaseinformation',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
