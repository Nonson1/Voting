# Generated by Django 4.0.2 on 2022-02-10 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_rename_github_url_userprofile_nin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='ward',
            field=models.CharField(max_length=100),
        ),
    ]