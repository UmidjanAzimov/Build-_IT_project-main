# Generated by Django 4.0.4 on 2022-05-18 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_alter_firmalar_litsenzya_alter_firmalar_logotip_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='firmalar',
            name='email_address',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='firmalar',
            name='mobile_number',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='firmalar',
            name='telegram_address',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
