# Generated by Django 3.1.2 on 2020-12-08 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopNow', '0008_auto_20201208_1007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myorder',
            name='productName',
        ),
        migrations.AddField(
            model_name='myorder',
            name='productName',
            field=models.ManyToManyField(related_name='productnames', to='ShopNow.Product'),
        ),
    ]
