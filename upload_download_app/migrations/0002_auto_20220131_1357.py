# Generated by Django 3.2.11 on 2022-01-31 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upload_download_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='organization_name',
            field=models.ForeignKey(max_length=25, on_delete=django.db.models.deletion.CASCADE, to='upload_download_app.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='organization_name',
            field=models.CharField(choices=[('SL', 'Sales'), ('MK', 'Marketing'), ('RD', 'Research And Develop'), ('IT', 'Information Technology')], max_length=25),
        ),
    ]
