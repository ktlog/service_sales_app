# Generated by Django 4.1.1 on 2022-10-07 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmsslider',
            name='cms_css',
            field=models.CharField(default='-', max_length=200, null=True, verbose_name='CSS класс'),
        ),
        migrations.AlterField(
            model_name='cmsslider',
            name='cms_img',
            field=models.ImageField(upload_to='sliderimg/'),
        ),
    ]
