# Generated by Django 4.1.1 on 2022-09-27 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galleria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userphoto',
            name='galleria',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='galleria.usergallery'),
        ),
    ]