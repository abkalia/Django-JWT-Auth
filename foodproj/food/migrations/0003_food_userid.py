# Generated by Django 3.1.6 on 2021-02-01 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20210201_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='userId',
            field=models.IntegerField(default=1),
        ),
    ]
