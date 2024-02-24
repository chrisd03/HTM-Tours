# Generated by Django 4.2.10 on 2024-02-24 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tourist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('age', models.IntegerField()),
                ('bio', models.TextField(verbose_name='Biography')),
                ('city', models.CharField(max_length=200, verbose_name='City')),
                ('state', models.CharField(max_length=200, verbose_name='State')),
                ('likes', models.JSONField(default=list)),
            ],
        ),
    ]
