# Generated by Django 2.2.7 on 2020-01-28 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0008_auto_20200128_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='databaseinformation',
            name='abv',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2),
            preserve_default=False,
        ),
    ]