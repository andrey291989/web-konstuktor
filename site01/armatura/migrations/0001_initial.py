# Generated by Django 2.1.1 on 2018-09-25 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='armatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diametr', models.CharField(max_length=3)),
                ('ves_armatury', models.CharField(max_length=5)),
                ('ploshad', models.CharField(max_length=5)),
            ],
        ),
    ]