# Generated by Django 3.2.5 on 2021-07-15 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tenant',
            old_name='first_name',
            new_name='First_name',
        ),
        migrations.RenameField(
            model_name='tenant',
            old_name='gender',
            new_name='Gender',
        ),
        migrations.RenameField(
            model_name='tenant',
            old_name='last_name',
            new_name='Last_name',
        ),
        migrations.AlterField(
            model_name='apartment',
            name='Number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='building',
            name='Number',
            field=models.CharField(max_length=500),
        ),
    ]
