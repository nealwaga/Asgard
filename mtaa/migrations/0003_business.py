# Generated by Django 4.0.5 on 2022-06-18 15:02

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mtaa', '0002_hood'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_photo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='b_photo')),
                ('b_name', models.CharField(blank=True, max_length=100, null=True)),
                ('b_description', models.TextField(blank=True, max_length=200, null=True)),
                ('b_email', models.CharField(blank=True, max_length=100, null=True)),
                ('hood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='biz', to='mtaa.hood')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]