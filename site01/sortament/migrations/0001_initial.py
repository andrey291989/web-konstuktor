# Generated by Django 2.1.1 on 2018-09-27 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='truby_gost_10704_91',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Diametr', models.IntegerField()),
                ('Tolshuna_stenki', models.IntegerField()),
                ('Ploshad_poperechnogo_sech', models.IntegerField()),
                ('Moment_inercii', models.IntegerField()),
                ('Moment_soprotivleniya', models.IntegerField()),
                ('Statisticheskiy_moment', models.IntegerField()),
                ('Radius_inercii', models.IntegerField()),
                ('Massa_v_pog_metre', models.IntegerField()),
            ],
        ),
    ]
