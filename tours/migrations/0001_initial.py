# Generated by Django 5.0.1 on 2024-02-24 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour_Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('bio', models.TextField(verbose_name='Biography')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('city', models.CharField(max_length=200, verbose_name='Home Town')),
                ('state', models.CharField(max_length=200, verbose_name='State')),
                ('country', models.CharField(max_length=200, verbose_name='Country')),
            ],
        ),
    ]
