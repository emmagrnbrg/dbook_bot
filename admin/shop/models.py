from django.db import models


class Category(models.Model):
    """
    Категории товаров
    """
    name = models.CharField(max_length=255, db_comment="Наименование категории")

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    """
    Подкатегории товаров
    """
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories',
        db_comment="Основная категория"
    )
    name = models.CharField(max_length=255, db_comment="Наименование подкатегории")

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Таблица товаров
    """
    name = models.CharField(max_length=255, db_comment="Наименование")
    description = models.TextField(blank=True, null=True, db_comment="Описание")
    price = models.IntegerField(db_comment="Цена (в копейках)")
    stock_quantity = models.IntegerField(default=0, db_comment="Количество в наличии")
    manufacturer = models.CharField(max_length=255, blank=True, null=True, db_comment="Производитель")
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, db_comment="Масса (г)")
    length = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, db_comment="Длина (см)")
    width = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, db_comment="Ширина (см)")
    height = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, db_comment="Высота (см)")
    production_year = models.PositiveIntegerField(blank=True, null=True, db_comment="Год выпуска")

    subcategories = models.ManyToManyField(
        'Subcategory',
        through='ProductSubcategory',
        related_name='products',
        db_comment="Подкатегории товара"
    )

    def __str__(self):
        return self.name


class ProductSubcategory(models.Model):
    """
    Подкатегории товаров ("многие-ко-многим", т.к. товар может принадлежать к разным подкатегориям)
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_comment="Товар")
    subcategory = models.ForeignKey('Subcategory', on_delete=models.CASCADE, db_comment="Подкатегория товара")

    class Meta:
        unique_together = ('product', 'subcategory')

    def __str__(self):
        return f"{self.product.name} — {self.subcategory.name}"


class ProductPhoto(models.Model):
    """
    Фото товаров
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='photos', db_comment="Товар")
    image = models.ImageField(upload_to='product_photos/', db_comment="Изображение (фото) товара")

    def __str__(self):
        return self.product.name
