# Generated by Django 3.2 on 2022-02-02 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_remove_siteconfig_favourite_icon'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SiteConfig',
        ),
    ]
