from django.db import models

class Post(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовка"
    )
    context = models.TextField(
        verbose_name="Описание"
    )
    created = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата создание"
    )
    status = models.BooleanField(
        default=True,
        verbose_name="Статус публикации"
    )
    cover = models.ImageField(
        default="image.jpg",
        upload_to="static",
        blank=True,
        verbose_name="Обложка"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class TeamMember(models.Model):
    name = models.CharField(
        max_length=260,
        verbose_name = "Команда"
    )
    role = models.CharField(
        max_length=255,
        verbose_name='Роль'
    )
    image = models.ImageField(
        default="image.jpg",
        upload_to="static",
        blank=True,
        verbose_name="Обложка"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Участник команды'
        verbose_name_plural = 'Участники команды'


class Courses(models.Model):
    front_end = models.TextField(
        verbose_name='Фронтенд'
    )
    back_end = models.TextField(
        verbose_name='бэкенд'
    )
    ux_ui = models.TextField(
        verbose_name='Дизайн разработчик'
    )
    android = models.TextField(
        verbose_name= 'андройд разработчик'
    )

    def __str__(self):
        return self.back_end

    class Meta:
        verbose_name = 'Курс програмирование'
        verbose_name_plural = 'Курсы програмирование'

class Front(models.Model): 
    front = models.TextField(
        verbose_name="Информация о Front-End Разработке"
    ) 
    def __str__(self):
        return self.android

    class Meta:
        verbose_name = "Информация о Фронтенд" 
        verbose_name_plural = "Информации о Фронтенд"      


class Back(models.Model):
    back = models.TextField(
        verbose_name="Информация о Back-End Разработке"
    )

    def __str__(self):
        return self.bakc
    
    class Meta:
        verbose_name = "Информация о Бэкенд" 
        verbose_name_plural = "Информации о Бэкенд"   


class Ux_ui(models.Model):
    ux_ui = models.TextField(
        verbose_name="Информация о UX/UI Разработке"
    )

    def __str__(self):
        return self.ux_ui
    
    class Meta:
        verbose_name = "Информация о Дизайн" 
        verbose_name_plural = "Информации о Дизайн"   


class Android(models.Model):
    android = models.TextField(
        verbose_name="Информация о Android Разработке"
    )

    def __str__(self):
        return self.android
    
    class Meta:
        verbose_name = "Информация о Андройд" 
        verbose_name_plural = "Информации о Андройд"   
    

class Benefist(models.Model):
    povtor = models.TextField(
        verbose_name="Повторное обучение"
    )
    main = models.TextField(
        verbose_name="Главный плюс"
    )
    image = models.ImageField(
        upload_to=True,
        verbose_name="Фотография преимущество"
    )

    def __str__(self):
        return self.main
    
    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"

