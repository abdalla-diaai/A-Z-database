# Generated by Django 5.1.3 on 2024-11-15 16:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0005_protocol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocol',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
