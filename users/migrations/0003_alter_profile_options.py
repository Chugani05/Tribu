# Generated by Django 5.1.2 on 2024-11-13 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['user__username']},
        ),
    ]
