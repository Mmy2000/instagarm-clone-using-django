# Generated by Django 3.1 on 2024-04-14 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import post.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, verbose_name='Tag')),
                ('slug', models.SlugField(default=uuid.uuid1, unique=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('picture', models.ImageField(upload_to=post.models.user_directory_path, verbose_name='Picture')),
                ('caption', models.CharField(max_length=10000, verbose_name='Caption')),
                ('posted', models.DateField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('tags', models.ManyToManyField(related_name='tags', to='post.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]