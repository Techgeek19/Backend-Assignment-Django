# Generated by Django 3.0.6 on 2020-08-16 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('outlet', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orders',
        ),
        migrations.DeleteModel(
            name='OrderUpdate',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
    ]
