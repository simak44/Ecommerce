from django.contrib import admin
from .models import (ProductModel, CategoryModel, BrandModel, AdditionalInformationModel, ReviewModel,
                     CustomerModel, CartModel, ProductDescriptionModel, ProductShortDescriptionModel, ProductImageModel)
# Register your models here.
@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'titleproduct', 'discription', 'actual_price', 'discounted_price', 
                    'product_image','p_category', 'p_brand', 'is_featured']

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']

@admin.register(BrandModel)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand']

@admin.register(CustomerModel)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['id', 'username', 'fname', 'lname', 'areacode', 'phone', 'address', 'zipcode']

@admin.register(CartModel)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'productid', 'quantity']

@admin.register(ProductDescriptionModel)
class ProductDescriptionAdmin(admin.ModelAdmin):
    # list_display = ['id', 'title', 'description']
    list_display = ['id', 'productid', 'title', 'titledescription', 'touch', 'touchdescription', 'camera', 'cameradescription', 'technology', 'technologydescription', 'design', 'designdescription' ]

@admin.register(ProductShortDescriptionModel)
class ShortDescriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'productname', 'description']

@admin.register(ProductImageModel)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'productid', 'productimage']

@admin.register(AdditionalInformationModel)
class AdditionalInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'productname','title', 'description']

@admin.register(ReviewModel)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'username','titleproduct', 'name', 'title', 'review', 'rating', 'date']