# Generated by Django 5.1.3 on 2024-11-15 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0003_remove_protocol_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='protocol',
            name='upload',
            field=models.FileField(blank=True, upload_to='docx/'),
        ),
    ]