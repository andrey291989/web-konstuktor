# Generated by Django 2.1.1 on 2018-10-08 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sortament', '0004_auto_20181008_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='gost_sortamenta',
            name='Gost_naz',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
