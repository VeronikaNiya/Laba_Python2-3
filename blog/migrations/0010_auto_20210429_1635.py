# Generated by Django 2.2.3 on 2021-04-29 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210429_1514'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Публікації', 'verbose_name_plural': 'Назва для публікацій'},
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='novels', verbose_name='Слаг'),
        ),
    ]
