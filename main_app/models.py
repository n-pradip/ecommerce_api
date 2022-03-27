from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='images',null=True,blank=True)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title