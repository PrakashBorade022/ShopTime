# Generated by Django 3.1.2 on 2020-12-08 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ShopNow', '0006_auto_20201208_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myorder',
            name='productName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product1', to='ShopNow.product'),
        ),
    ]