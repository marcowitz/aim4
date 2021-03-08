# Generated by Django 3.1.7 on 2021-03-08 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0007_auto_20210308_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='velocity',
            field=models.FloatField(default=0, verbose_name='Velocity'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='distance',
            field=models.FloatField(default=0, verbose_name='Distance'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='target_distance',
            field=models.IntegerField(default=0, verbose_name='Target distance in Km'),
        ),
    ]
