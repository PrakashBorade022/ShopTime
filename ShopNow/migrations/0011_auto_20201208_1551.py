# Generated by Django 3.1.2 on 2020-12-08 15:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ShopNow', '0010_auto_20201208_1105'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyOrder',
            new_name='MyCart',
        ),
    ]
