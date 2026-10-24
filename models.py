from django.db import models

# Create your models here.
from django.db import models


class Customer(models.Model):
    customer_number = models.CharField(
        max_length=20,
        unique=True
    )

    name = models.CharField(
        max_length=100
    )

    def __str__(self):
        return f"{self.customer_number} - {self.name}"


class Item(models.Model):
    item_number = models.CharField(
        max_length=20,
        unique=True
    )

    description = models.CharField(
        max_length=200
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.item_number} - {self.description}"


class Invoice(models.Model):
    customer_number = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=100)

    items = models.JSONField()

    memo = models.TextField(blank=True)

    total = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice {self.id} - {self.customer_number}"
