# Generated by Django 3.0.3 on 2020-04-11 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_title', models.CharField(max_length=100)),
                ('details', models.TextField(max_length=500)),
            ],
        ),
    ]
