# Generated by Django 3.0 on 2019-12-08 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courtAPI', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courtdetail',
            old_name='court',
            new_name='court1',
        ),
        migrations.RenameField(
            model_name='courtdetail',
            old_name='proceedingType',
            new_name='proceedingType1',
        ),
        migrations.AddField(
            model_name='courtdetail',
            name='court2',
            field=models.CharField(default='-', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courtdetail',
            name='court3',
            field=models.CharField(default='-', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courtdetail',
            name='proceedingType2',
            field=models.CharField(default='-', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courtdetail',
            name='proceedingType3',
            field=models.CharField(default='-', max_length=200),
            preserve_default=False,
        ),
    ]
