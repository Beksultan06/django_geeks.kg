# Generated by Django 4.2.4 on 2023-08-18 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовка')),
                ('context', models.TextField(verbose_name='Описание')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Дата создание')),
                ('status', models.BooleanField(default=True, verbose_name='Статус публикации')),
                ('cover', models.ImageField(blank=True, default='image.jpg', upload_to='upload/posts', verbose_name='Обложка')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]