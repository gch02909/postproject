# Generated by Django 2.2.5 on 2019-11-04 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0004_auto_20191010_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='usr'),
        ),
    ]
