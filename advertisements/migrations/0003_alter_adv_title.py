# Generated by Django 4.2.4 on 2023-08-27 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0002_alter_adv_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adv',
            name='title',
            field=models.CharField(max_length=80, verbose_name='name'),
        ),
    ]