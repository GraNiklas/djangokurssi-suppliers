from django.db import models

class Supplier(models.Model):
    companyname = models.CharField(max_length=50, default="firma")
    contactname = models.CharField(max_length=50, default="firma")
    address = models.CharField(max_length=50, default="firma")
    phone = models.CharField(max_length=50, default="firma")
    email = models.CharField(max_length=50, default="firma")
    country = models.CharField(max_length=50, default="firma")
    def __str__(self):
        return f"{self.companyname} from {self.country}"

class Product(models.Model):
    productname = models.CharField(max_length=50, default="product")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stock = models.IntegerField(default=0)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.productname} from {self.supplier.companyname}"