from django.db import models
import datetime
from django.contrib.auth.models import User



class CategoryModel(models.Model):
    category = models.CharField(max_length = 100)
    def __str__(self):
        return self.category
    
class BrandModel(models.Model):
    brand = models.CharField(max_length= 100)
    def __str__(self):
        return self.brand


class ProductModel(models.Model):
    titleproduct = models.CharField(max_length=100)
    discription = models.CharField(max_length=100)
    actual_price = models.FloatField()
    discounted_price = models.FloatField()
    product_image = models.ImageField(upload_to='productimg')
    p_category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    p_brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    is_featured = models.BooleanField(default = False)
    def __str__(self):
        return str(self.id)
    # def __str__(self):
    #     return f'{self.id},{self.titleproduct}'
   
        
class CustomerModel(models.Model):
    username = models.ForeignKey(User, on_delete = models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100, default=None)
    areacode = models.IntegerField(default = None)
    phone = models.IntegerField(default = None)
    address = models.CharField(max_length=100)
    zipcode =  models.IntegerField(default = None)


class CartModel(models.Model):
    username = models.ForeignKey(User, on_delete = models.CASCADE)
    productid = models.ForeignKey(ProductModel, on_delete= models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_pric(self):
       return int((self.quantity*self.productid.discounted_price))
    


class ProductDescriptionModel(models.Model):
    productid = models.ForeignKey(ProductModel, on_delete = models.CASCADE)
    title = models.CharField(max_length = 20, default = None)
    titledescription = models.CharField(max_length = 500, default = None)
    touch = models.CharField(max_length = 20, default = None)
    touchdescription = models.CharField(max_length = 500, default = None)
    camera = models.CharField(max_length = 20, default = None)
    cameradescription = models.CharField(max_length = 500, default = None)
    technology = models.CharField(max_length = 20, default = None)
    technologydescription = models.CharField(max_length = 500, default = None)
    design = models.CharField(max_length = 20, default = None)
    designdescription = models.CharField(max_length = 500, default = None)

class ProductShortDescriptionModel(models.Model):
    productname = models.ForeignKey(ProductModel, on_delete = models.CASCADE)
    description = models.TextField(default=None)
    

class AdditionalInformationModel(models.Model):
    productname = models.ForeignKey(ProductModel, on_delete = models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()


class ReviewModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    titleproduct = models.ForeignKey(ProductModel,on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    review = models.TextField()
    rating = models.IntegerField()
    date = models.DateTimeField( auto_now_add = True)

    def ratingbtw(self):
        if self.rating < 0:
            ValueError('value should be greater than 0')
        elif self.rating > 5:
            ValueError('value should be greater than 0')
        else:
            return self.rating
        
    # def value(self):
    #     return self.username == self.request.user