# Generated by Django 5.1.3 on 2024-11-20 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0008_alter_experiment_methods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='methods',
            field=models.TextField(blank=True, null=True),
        ),
    ]