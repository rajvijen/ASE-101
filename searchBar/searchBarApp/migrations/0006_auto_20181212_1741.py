# Generated by Django 2.1.2 on 2018-12-12 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchBarApp', '0005_auto_20181212_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
        ),
    ]
