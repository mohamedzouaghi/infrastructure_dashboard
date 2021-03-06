# Generated by Django 3.0.6 on 2020-05-14 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0003_auto_20200514_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='serverdetails',
            name='server_name',
            field=models.CharField(default='', max_length=200, verbose_name='Server Name'),
        ),
        migrations.AlterField(
            model_name='serverdetails',
            name='seperate_bill_file',
            field=models.ImageField(blank=True, null=True, upload_to='bills', verbose_name='Bill file'),
        ),
    ]
