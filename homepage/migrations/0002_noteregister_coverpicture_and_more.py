# Generated by Django 4.0.3 on 2022-03-21 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noteregister',
            name='coverpicture',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='noteregister',
            name='title_page',
            field=models.CharField(default='type', max_length=30),
        ),
    ]