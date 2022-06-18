from django.db import models
from account.models import Account

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.category_name

class Product(models.Model):
    seller = models.ForeignKey(Account, on_delete=models.CASCADE)
    product_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    product_title = models.CharField(max_length=150)
    product_cost = models.PositiveIntegerField(default=1000)
    product_description = models.TextField(max_length=500)
    product_image = models.FileField(upload_to='product files/')
    added_time = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.seller.first_name} {self.seller.last_name}: {self.product_title} - {self.product_category.category_name}"

class Capital(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    capital_percent = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name_plural = "Capital"

    def __str__(self):
        return self.product.product_title

class Box(models.Model):
    buyer = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_number = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.buyer.username} - {self.product.product_title}"

class Recommended(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.product_title