# Generated by Django 3.1.2 on 2020-12-08 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopNow', '0009_auto_20201208_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myorder',
            name='productName',
            field=models.ManyToManyField(null=True, related_name='productnames', to='ShopNow.Product'),
        ),
    ]
