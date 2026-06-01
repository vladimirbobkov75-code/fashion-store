from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название категории"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Название товара"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория"
    )

    description = models.TextField(
        verbose_name="Описание"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена"
    )

    image = models.ImageField(
        upload_to='products/',
        verbose_name="Изображение"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class ContactRequest(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Имя клиента"
    )

    phone = models.CharField(
        max_length=20,
        verbose_name="Телефон"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"