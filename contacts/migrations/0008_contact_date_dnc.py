# Generated by Django 4.2.1 on 2024-07-22 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0007_contact_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="date_dnc",
            field=models.DateField(blank=True, null=True),
        ),
    ]
