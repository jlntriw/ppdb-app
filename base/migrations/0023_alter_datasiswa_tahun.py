# Generated by Django 4.2.5 on 2023-10-09 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_alter_datasiswa_tahun'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasiswa',
            name='tahun',
            field=models.DateField(auto_now_add=True, verbose_name='Tahun'),
        ),
    ]