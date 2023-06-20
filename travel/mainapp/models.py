from django.db import models


# Create your models here.

class News(models.Model):
    name = models.CharField(verbose_name='Название новости', max_length=120)
    image = models.ImageField(verbose_name='Изображение новости', upload_to='news/%Y/%m/%d')
    description = models.CharField(verbose_name='Описание новости', max_length=300  )

    backround = models.ImageField(verbose_name='Фон главного экрана', upload_to='bg/%Y/%m/%d', blank=True)
    detailed_desc = models.CharField(verbose_name='Подробное описание', max_length=10000, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Hotels(models.Model):
    name = models.CharField(verbose_name='Название отеля', max_length=120)
    image = models.ImageField(verbose_name='Изображение отеля', upload_to='hotels/%Y/%m/%d')
    description = models.CharField(verbose_name='Описание отеля', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'


class Tour(models.Model):
    name = models.CharField(verbose_name='Страна', max_length=120)
    second_name = models.CharField(verbose_name='Название тура', max_length=120, default=0)
    image = models.ImageField(verbose_name='Изображение', upload_to='tour/%Y/%m/%d', blank=True)

    backround = models.ImageField(verbose_name='Фон главного экрана', upload_to='bg/%Y/%m/%d', blank=True)
    price = models.IntegerField(verbose_name='Цена', default=0)
    description = models.TextField(verbose_name='Описание тура')
    conditions = models.TextField(verbose_name='Условия тура')
    hotels = models.ManyToManyField(Hotels, verbose_name='Отели')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'


class FeedBack(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=256)
    last_name = models.CharField(verbose_name='Фамилия', max_length=256)
    email = models.EmailField(verbose_name='Электронная почта')
    select = models.ForeignKey(Tour, verbose_name='Выберите страну', on_delete=models.CASCADE, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'


