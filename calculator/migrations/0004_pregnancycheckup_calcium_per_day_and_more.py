# Generated by Django 5.1.1 on 2024-11-16 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0003_checkupvisit_total_calcium_checkupvisit_total_iron'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregnancycheckup',
            name='calcium_per_day',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pregnancycheckup',
            name='iron_per_day',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
