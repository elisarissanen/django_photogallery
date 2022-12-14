from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import galleria.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGallery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('private', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('owner', models.ForeignKey(default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        
        migrations.CreateModel(
            name='UserPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=galleria.models.user_directory_path)),
                ('description', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('galleria', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='galleria.usergallery')),
                ('owner', models.ForeignKey(default=django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
