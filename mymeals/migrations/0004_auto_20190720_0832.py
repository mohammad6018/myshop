# Generated by Django 2.2.3 on 2019-07-20 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymeals', '0003_auto_20190720_0818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='pub_date',
            field=models.DateField(auto_now=True),
        ),
    ]
