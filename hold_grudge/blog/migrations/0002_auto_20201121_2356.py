# Generated by Django 3.1.2 on 2020-11-21 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='is_bav',
            new_name='is_nav',
        ),
    ]