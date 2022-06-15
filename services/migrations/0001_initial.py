# Generated by Django 3.2 on 2022-06-15 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Civil Engineering Structures', 'Civil Engineering Structures'), ('External Fire Risk Inspections', 'External Fire Risk Inspections'), ('Domestic & Commercial Surveys - Chimney & Roof Inspections', 'Domestic & Commercial Surveys - Chimney & Roof Inspections'), ('Domestic & Commercial Surveys - Roof Inspections All Areas', 'Domestic & Commercial Surveys - Roof Inspections All Areas'), ('Domestic & Commercial Surveys - Gutter & Roof Inspections', 'Domestic & Commercial Surveys - Gutter & Roof Inspections'), ('Domestic & Commercial Surveys - Dangerous Structures Inspections', 'Domestic & Commercial Surveys - Dangerous Structures Inspections')], max_length=254)),
                ('friendly_name', models.CharField(choices=[('CES', 'CES'), ('EFRI', 'EFRI'), ('D&CS I', 'D&CS I'), ('D&CS II', 'D&CS II'), ('D&CS III', 'D&CS III'), ('D&CS IV', 'D&CS IV')], max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(choices=[('Civil Engineering Structures', 'CES'), ('External Fire Risk Inspections', 'EFRI'), ('Domestic & Commercial Surveys - Chimney & Roof Inspections', 'D&CS I'), ('Domestic & Commercial Surveys - Roof Inspections All Areas', 'D&CS II'), ('Domestic & Commercial Surveys - Gutter & Roof Inspections', 'D&CS III'), ('Domestic & Commercial Surveys - Dangerous Structures Inspections', 'D&CS IV')], max_length=254)),
                ('includes', models.CharField(choices=[('Pre-site survey and Risk Assessment, Drone Survey of intended area & Photos', 'Pre-site survey and Risk Assessment, Drone Survey of intended area & Photos'), ('Pre-site survey and Risk Assessment, Drone Survey of intended area, Videos & Photos', 'Pre-site survey and Risk Assessment, Drone Survey of intended area, Videos & Photos'), ('Pre-site survey and Risk Assessment, Drone Survey of intended area, Videos, Photos & Thermal Imaging', 'Pre-site survey and Risk Assessment, Drone Survey of intended area, Videos, Photos & Thermal Imaging'), ('Pre-site survey and Risk Assessment, Drone Survey of intended area, Editied Video Presentation & Recommendations of Works Required', 'Pre-site survey and Risk Assessment, Drone Survey of intended area, Editied Video Presentation & Recommendations of Works Required'), ('Pre-site survey and Risk Assessment, Drone Survey of intended area & Surveyor Report', 'Pre-site survey and Risk Assessment, Drone Survey of intended area & Surveyor Report')], max_length=254)),
                ('description', models.CharField(choices=[('Drone survey with photos', 'Drone survey with photos'), ('Drone survey with Video & photos', 'Drone survey with Video & photos'), ('Drone survey with videos & photos with thermal images', 'Drone survey with videos & photos with thermal images'), ('Drone survey edited version & recommendations of work', 'Drone survey edited version & recommendations of work'), ('Drone survey with surveyor report', 'Drone survey with surveyor report')], max_length=254)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('spotters', models.DecimalField(decimal_places=2, default=150, max_digits=6)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Services',
            },
        ),
    ]
