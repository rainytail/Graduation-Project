# Generated by Django 5.0.4 on 2024-04-19 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vueApi', '0003_usershare_shareid_alter_usershare_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='usershare',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]