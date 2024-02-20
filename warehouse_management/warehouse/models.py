from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Название категории'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    class Mete:
        verbose_name = 'Категория'

    def __str__(self):
        return self.title


class Provider(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Наименование компании'
    )
    contact_person = models.CharField(
        max_length=256,
        verbose_name='Контактное лицо'
    )
    address = models.CharField(
        max_length=300,
        verbose_name='Адрес'
    )
    phone = models.CharField(
        max_length=12,
        verbose_name='Телефон'
    )

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Наименование товара'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Количество'
    )
    provider = models.ForeignKey(
        'Provider',
        on_delete=models.SET_NULL,
        null=True,
    )

    def get_fields(self):
        return [
            self.id,
            self.title,
            self.category,
            self.description,
            self.quantity,
            self.provider
        ]


    def __str__(self):  
        return self.title
