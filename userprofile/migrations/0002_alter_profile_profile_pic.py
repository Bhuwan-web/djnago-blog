# Generated by Django 4.0.1 on 2022-02-07 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]