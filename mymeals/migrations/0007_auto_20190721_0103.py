# Generated by Django 2.2.3 on 2019-07-21 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymeals', '0006_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
