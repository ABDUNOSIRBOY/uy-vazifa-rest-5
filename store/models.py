from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    title = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    warranty_period = models.IntegerField(default=1) # yil hisobida

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    purchased_product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    address = models.TextField()
    bought_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name