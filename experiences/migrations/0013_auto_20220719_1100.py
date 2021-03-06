# Generated by Django 3.2 on 2022-07-19 11:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0012_auto_20220719_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='employment',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employment',
            name='start_year',
            field=models.CharField(default='January', max_length=255, verbose_name='Start Year'),
        ),
    ]
