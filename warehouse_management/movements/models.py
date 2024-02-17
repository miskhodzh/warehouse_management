from django.db import models
from django.utils import timezone

STATUS_CHOICES = (
        ('add', 'Добаленно'),
        ('move', 'Прошло'),
    )

class ReceiptInvoice(models.Model):
    date_creation = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата создания'
    )
    date_move = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Дата проверки'
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='новая',
        verbose_name='Статус'
    )


