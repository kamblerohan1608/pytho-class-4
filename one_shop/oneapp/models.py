from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    product_catagory = models.CharField(max_length=100)
    catagory_image = models.ImageField(upload_to = 'category_image')

    def __str__(self):
        return self.product_catagory

class ProductModel(models.Model):
    p_category = models.ForeignKey(ProductCategory,on_delete =models.CASCADE)
    p_name = models.CharField(max_length=100)
    p_desc = models.TextField(blank=True)
    p_brand = models.CharField(max_length=100)
    p_price = models.PositiveIntegerField()
    p_image = models.ImageField(upload_to = 'product_image/')

    def __str__(self):
        return (f"{self.p_category} {self.p_name} {self.p_price}")