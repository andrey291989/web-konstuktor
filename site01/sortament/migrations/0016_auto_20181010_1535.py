# Generated by Django 2.1.1 on 2018-10-10 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sortament', '0015_auto_20181010_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gost_sortamenta',
            name='img_gost',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
