# Generated by Django 5.1.7 on 2025-03-21 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='added_at',
        ),
    ]
