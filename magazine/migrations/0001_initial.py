# Generated by Django 4.1 on 2022-08-11 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('photo_magazine', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменнения')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL')),
                ('categor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='magazine.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Книги',
                'verbose_name_plural': 'Книги',
                'ordering': ['time_create'],
            },
        ),
    ]
