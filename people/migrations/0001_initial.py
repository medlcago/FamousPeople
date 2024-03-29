# Generated by Django 5.0.2 on 2024-02-26 11:01

import django.db.models.deletion
import django_extensions.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Категория')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=255, populate_from='name', unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Celebrity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Заголовок')),
                ('content', models.TextField(blank=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')),
                ('is_published', models.BooleanField(choices=[(False, 'Черновик'), (True, 'Опубликовано')], default=0, verbose_name='Статус')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=255, populate_from='title', unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='people.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Знаменитость',
                'verbose_name_plural': 'Знаменитости',
                'ordering': ('-created_at',),
            },
        ),
    ]
