# Generated by Django 4.1.3 on 2022-11-12 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_category_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='thumbnail',
            new_name='image',
        ),
    ]