# Generated by Django 3.1.2 on 2020-12-09 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShopNow', '0015_remove_myorder2_orderby'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyOrder2',
        ),
    ]