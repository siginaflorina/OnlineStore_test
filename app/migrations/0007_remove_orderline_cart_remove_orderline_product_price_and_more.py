# Generated by Django 4.1.3 on 2022-11-21 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_profile_img_user_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderline',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='orderline',
            name='product_price',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
