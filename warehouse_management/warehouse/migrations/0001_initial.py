# Generated by Django 3.2 on 2024-02-15 22:47

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
                ('title', models.CharField(max_length=256, verbose_name='Название категории')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Наименование компании')),
                ('contact_person', models.CharField(max_length=256, verbose_name='Контактное лицо')),
                ('address', models.CharField(max_length=300, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=12, verbose_name='Телефон')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Наименование товара')),
                ('description', models.TextField(verbose_name='Описание')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='warehouse.category')),
                ('provider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='warehouse.provider')),
            ],
        ),
    ]