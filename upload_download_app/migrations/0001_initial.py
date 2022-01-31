# Generated by Django 3.2.11 on 2022-01-31 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=10)),
                ('organization_files', models.FileField(upload_to='uploaded_files/')),
                ('file_dlnumber', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('organization_name', models.ForeignKey(max_length=10, on_delete=django.db.models.deletion.CASCADE, to='upload_download_app.organization')),
            ],
        ),
    ]