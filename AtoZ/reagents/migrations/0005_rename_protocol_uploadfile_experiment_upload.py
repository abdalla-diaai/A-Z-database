# Generated by Django 5.1.3 on 2024-11-17 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0004_protocol_upload'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Protocol',
            new_name='UploadFile',
        ),
        migrations.AddField(
            model_name='experiment',
            name='upload',
            field=models.FileField(blank=True, upload_to='docx/'),
        ),
    ]
