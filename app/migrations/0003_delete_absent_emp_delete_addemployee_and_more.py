# Generated by Django 4.1.7 on 2023-03-20 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_quote_remove_leave_app_absentemp_status_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Absent_emp',
        ),
        migrations.DeleteModel(
            name='Addemployee',
        ),
        migrations.DeleteModel(
            name='Admin_Login',
        ),
        migrations.DeleteModel(
            name='CompanySetup',
        ),
        migrations.DeleteModel(
            name='Leave_App',
        ),
        migrations.DeleteModel(
            name='Leave_Policy',
        ),
        migrations.DeleteModel(
            name='Quote',
        ),
        migrations.AddField(
            model_name='event',
            name='visibility',
            field=models.BooleanField(default=False),
        ),
    ]
