# Generated by Django 5.0.2 on 2024-02-24 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_tour_guide_phone_number_tour_guide_years_lived_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour_guide',
            name='likes',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='tour_guide',
            name='phone_number',
            field=models.CharField(default='', max_length=10, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='tourist',
            name='phone_number',
            field=models.CharField(default='', max_length=10, verbose_name='Phone Number'),
        ),
    ]
