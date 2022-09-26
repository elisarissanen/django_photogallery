# Generated by Django 4.1.1 on 2022-09-26 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galleria', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usergallery',
            name='id',
        ),
        migrations.AlterField(
            model_name='usergallery',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='galleria.user'),
        ),
    ]