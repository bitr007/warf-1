# Generated by Django 3.1.7 on 2021-05-12 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0003_scan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scan',
            name='scan_type',
            field=models.CharField(choices=[('Full Scan', 'Full Scan'), ('Subdomain', 'Subdomain'), ('Dirsearch', 'Dirsearch'), ('Wayback URL', 'Wayback URL'), ('JS File Discovery', 'JS File Discovery'), ('Secret/API key', 'Secret/API key'), ('Endpoint from JS', 'Endpoint from JS')], max_length=50),
        ),
    ]
