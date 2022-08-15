# Generated by Django 3.2 on 2022-07-11 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserAccount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "contact_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("address1", models.CharField(blank=True, max_length=80, null=True)),
                ("address2", models.CharField(blank=True, max_length=80, null=True)),
                ("post_code", models.CharField(blank=True, max_length=20, null=True)),
                ("city", models.CharField(blank=True, max_length=40, null=True)),
                ("county", models.CharField(blank=True, max_length=80, null=True)),
                (
                    "country",
                    django_countries.fields.CountryField(
                        blank=True, max_length=2, null=True
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
