# Generated by Django 4.2.7 on 2024-02-12 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reagents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CellLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cell_name', models.CharField(blank=True, max_length=300, null=True)),
                ('media', models.CharField(blank=True, max_length=300, null=True)),
                ('genotype', models.CharField(choices=[('Wildtype', True), ('Modified', False)], default=True, max_length=30)),
                ('storage_position', models.CharField(blank=True, max_length=10, null=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]