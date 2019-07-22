# Generated by Django 2.2.3 on 2019-07-21 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymeals', '0005_auto_20190720_0834'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Shirts & Tops', 'Shirts & Tops'), ('Dresses', 'Dresses'), ('Shorts & Skirts', 'Shorts & Skirts'), ('Jackets', 'Jackets'), ('Coats', 'Coats'), ('Sleeveless', 'Sleeveless'), ('Trousers', 'Trousers'), ('Winter Coats', 'Winter Coats'), ('Jumpsuits', 'Jumpsuits')], default='Shirts & Tops', max_length=20)),
            ],
        ),
    ]
