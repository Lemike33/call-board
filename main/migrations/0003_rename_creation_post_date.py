# Generated by Django 4.1.7 on 2023-02-17 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='creation',
            new_name='date',
        ),
    ]
