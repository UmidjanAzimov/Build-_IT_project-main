# Generated by Django 4.0.4 on 2022-05-18 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_firmalar_litsenzya_alter_firmalar_logotip_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firmalar',
            name='litsenzya',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='firmalar',
            name='logotip',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='firmalar',
            name='portfolio',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
