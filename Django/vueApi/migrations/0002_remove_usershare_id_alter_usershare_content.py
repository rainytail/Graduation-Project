# Generated by Django 5.0.4 on 2024-04-19 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vueApi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usershare',
            name='id',
        ),
        migrations.AlterField(
            model_name='usershare',
            name='content',
            field=models.CharField(max_length=1000, primary_key=True, serialize=False),
        ),
    ]