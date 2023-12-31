# Generated by Django 4.2.4 on 2023-08-19 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_android'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('povtor', models.TextField(verbose_name='Повторное обучение')),
                ('main', models.TextField(verbose_name='Главный плюс')),
            ],
            options={
                'verbose_name': 'Преимущество',
                'verbose_name_plural': 'Преимущества',
            },
        ),
        migrations.AlterModelOptions(
            name='android',
            options={'verbose_name': 'Информация о Андройд', 'verbose_name_plural': 'Информации о Андройд'},
        ),
        migrations.AlterModelOptions(
            name='back',
            options={'verbose_name': 'Информация о Бэкенд', 'verbose_name_plural': 'Информации о Бэкенд'},
        ),
        migrations.AlterModelOptions(
            name='front',
            options={'verbose_name': 'Информация о Фронтенд', 'verbose_name_plural': 'Информации о Фронтенд'},
        ),
        migrations.AlterModelOptions(
            name='ux_ui',
            options={'verbose_name': 'Информация о Дизайн', 'verbose_name_plural': 'Информации о Дизайн'},
        ),
        migrations.RenameField(
            model_name='back',
            old_name='bakc',
            new_name='back',
        ),
    ]
