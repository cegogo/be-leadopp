# Generated by Django 5.0.6 on 2024-06-26 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0016_alter_user_first_name_alter_user_job_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.TextField(blank=True, null=True),
        ),
    ]
