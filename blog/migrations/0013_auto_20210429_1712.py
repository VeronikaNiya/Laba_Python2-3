# Generated by Django 2.2.3 on 2021-04-29 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20210429_1657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='slug',
            new_name='slug_in',
        ),
    ]