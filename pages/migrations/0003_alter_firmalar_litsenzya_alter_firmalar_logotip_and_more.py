# Generated by Django 4.0.4 on 2022-05-17 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_mutaxasis_lavozim_alter_mutaxasis_yonalish'),
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
