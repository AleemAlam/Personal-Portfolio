# Generated by Django 3.0.3 on 2020-04-11 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalapp', '0002_myproject'),
    ]

    operations = [
        migrations.AddField(
            model_name='addservices',
            name='iconclass',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
