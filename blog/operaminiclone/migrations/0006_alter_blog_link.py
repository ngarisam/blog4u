# Generated by Django 4.2.6 on 2023-10-29 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operaminiclone', '0005_alter_blog_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='link',
            field=models.CharField(max_length=150, null=True),
        ),
    ]