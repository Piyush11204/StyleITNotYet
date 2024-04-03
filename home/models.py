from django.db import models

# Create your models here.
class ShopIT(models.Model):
    name = models.CharField(max_length=255)
    price =  models.DecimalField(max_length=10, decimal_places=2,max_digits=7)
    # category= models.ForeignKey('Category',on_delete=models.CASCADE ,null=True,blank=True)
    # description = models.CharField(max_length=255 , null= True , blank=True , default="This product does not have a description.")
    quantity = models.PositiveIntegerField(default=1)
    img  = models.ImageField(upload_to='Uploaded/' ,max_length=None)
    
    def __str__(self):
        return self.name + ' - $' + str(self.price)
        

# class Category(models.Model):
#     name = models.CharField(max_length=30)
    
    
    
