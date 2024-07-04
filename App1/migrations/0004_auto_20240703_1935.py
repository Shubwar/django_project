# Generated by Django 3.0 on 2024-07-03 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_auto_20240621_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='date_joined',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='is_deleted',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='mobile_num',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]