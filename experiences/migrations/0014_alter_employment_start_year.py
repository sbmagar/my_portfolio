# Generated by Django 3.2 on 2022-07-19 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0013_auto_20220719_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employment',
            name='start_year',
            field=models.CharField(default='2020', max_length=255, verbose_name='Start Year'),
        ),
    ]