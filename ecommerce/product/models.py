from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# class Category(MPTTModel):
#     name = models.CharField(max_length=100)
#     parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

#     class MPTTMeta:
#         order_insertion_by = ["name"]

#     def __str__(self):
#         return self.name

class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    Category = TreeForeignKey('Category', on_delete=models.SET_DEFAULT,default=1, null=True, blank=True)

    def __str__(self):
        return self.name