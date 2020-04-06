# Generated by Django 2.2.7 on 2020-02-26 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0021_stouts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(max_length=2000, null=True)),
                ('abv', models.FloatField()),
                ('img', models.CharField(max_length=100, null=True)),
                ('rating', models.IntegerField(default=3)),
            ],
        ),
    ]
