# Generated by Django 3.0.3 on 2020-02-28 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='lineons',
            new_name='linenos',
        ),
    ]
