# Generated by Django 4.2.5 on 2023-10-04 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_datasiswa_alamat'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasiswa',
            name='tahun',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
