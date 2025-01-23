from django.db import models

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # A unique name for the category
    description = models.TextField(blank=True, null=True)  # Optional description of the category

    def __str__(self):
        return self.name  # This returns the category name as a string representation


# Product Model
class Product(models.Model):
    name = models.CharField(max_length=100)  # Product name
    description = models.TextField(blank=True, null=True)  # Optional product description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price with up to 2 decimal places
    category = models.ForeignKey(  # Relationship to Category
        Category,
        on_delete=models.CASCADE,  # Delete products if the category is deleted
        related_name='products'  # Allows reverse lookup (category.products)
    )
    stock = models.PositiveIntegerField()  # Number of items in stock (must be non-negative)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the product is created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when the product is updated

    def __str__(self):
        return self.name  # This returns the product name as a string representation
