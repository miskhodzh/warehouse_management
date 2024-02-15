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

