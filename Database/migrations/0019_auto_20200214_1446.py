# Generated by Django 2.2.7 on 2020-02-14 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0018_databaseinformation_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='RankedDatabase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(max_length=2000, null=True)),
                ('abv', models.FloatField()),
                ('img', models.CharField(max_length=100, null=True)),
                ('like', models.IntegerField(null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='databaseinformation',
            old_name='rate',
            new_name='like',
        ),
    ]
