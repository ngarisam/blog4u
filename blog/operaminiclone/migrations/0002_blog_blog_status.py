# Generated by Django 4.2.6 on 2023-10-29 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operaminiclone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_status',
            field=models.CharField(choices=[('pending', 'pending'), ('revise', 'revise'), ('published', 'published'), ('rejected', 'rejected')], default='pending', max_length=10),
        ),
    ]
