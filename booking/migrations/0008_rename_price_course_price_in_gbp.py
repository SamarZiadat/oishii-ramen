# Generated by Django 3.2.19 on 2023-05-16 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_rename_duration_course_duration_in_hrs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='price',
            new_name='price_in_gbp',
        ),
    ]
