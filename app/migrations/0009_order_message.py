# Generated by Django 4.1.3 on 2022-11-21 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_order_status_alter_order_total_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='message',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
