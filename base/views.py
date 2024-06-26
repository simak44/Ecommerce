from typing import Any
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views import View
from .forms import AddressForm, ReviewForm
from django.views.generic import ListView, FormView, DetailView, TemplateView, DeleteView
from .models import (ProductModel, CategoryModel, CustomerModel, AdditionalInformationModel, ReviewModel,
                     CartModel, BrandModel, ProductDescriptionModel, ProductShortDescriptionModel, ProductImageModel)
from django.db.models.aggregates import Sum
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.conf import settings
import random
import stripe
import os
stripe.api_key = settings.STRIPE_SECRET_KEY




# Create your views here.

# This View is for Dashboard/Home
# def shutdownPC(request):
#    os.system("shutdown /s /t 1")
#    return request

class IndexView(TemplateView):
    model = ProductModel
    template_name = "base/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feature'] = ProductModel.objects.filter(is_featured = True)
        context['mobile'] = ProductModel.objects.filter(p_category__category = 'MobilePhones')
        context['tablet'] = ProductModel.objects.filter(p_category__category = 'Tablet')
        context['randoms'] = ProductModel.objects.all()[:3]
      #   context['randoms']

      #   for rando in randoms:
      #      context['rando'] = rando
      #    #   rando = context['rando']
      #      print(context['rando'])
      #   context['randoms'] = random.choices(rando, k=3)
        context['brand'] = BrandModel.objects.all( )
        context['category'] = CategoryModel.objects.all()
        if self.request.user.is_authenticated:
         context['cart'] = CartModel.objects.filter(username=self.request.user)
        return context
    
class ShowAllView(ListView):
   model = ProductModel
   template_name = 'base/product.html'
   context_object_name="items"
   paginate_by = 3
   ordering = ['id']
   def get_context_data(self, **kwargs: Any):
      kwrd = self.kwargs['p_brand']
      print(kwrd)
      # if kwrd== 'p_category':
      items= ProductModel.objects.filter(Q(p_category__category__contains = kwrd) | Q(p_brand__brand__contains= kwrd))
      # print(items.count())
      context = super(ShowAllView, self).get_context_data(object_list=items, **kwargs)
      context['count']=items.count()
      # print(context['items'])
      # elif kwrd == 'p_brand': 
      #    context['items'] = ProductModel.objects.filter(p_category__category = 'Tablet')
      # elif kwrd == 'p_brand':
         # context['items'] = ProductModel.objects.filter(p_brand__brand = 'p_brand')
      context['kwrd']= kwrd
      context['brand'] = BrandModel.objects.all( )
      context['category'] = CategoryModel.objects.all()
      context['cart'] = CartModel.objects.filter(username=self.request.user)
      return context
   
class SearchView(ListView):
   model=ProductModel
   context_object_name="items"
   paginate_by = 3
   ordering = ['id']
   template_name = 'base/product.html'
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      kwrd = self.request.GET.get("keyword")
      # kwrd = self.request.GET.get("price_from")
      # kwrd1 = self.request.GET.get("price_to")
      print("my>>",kwrd)
      items= ProductModel.objects.filter(Q(titleproduct__contains = kwrd) | Q(p_category__category__contains=kwrd)|
                                                    Q(p_brand__brand__contains = kwrd))
      context = super(SearchView, self).get_context_data(object_list=items, **kwargs)
      context['count']=context['items'].count()
      context['kwrd']= kwrd
      context['brand'] = BrandModel.objects.all( )
      context['category'] = CategoryModel.objects.all()
      context['cart'] = CartModel.objects.filter(username=self.request.user)
      return context

class TabletView(TemplateView):
    model = ProductModel
    template_name = 'base/tablet.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['feature'] = ProductModel.objects.filter(is_featured = True)
        context['brand'] = BrandModel.objects.all( )
        context['category'] = CategoryModel.objects.all()
        context['cart'] = CartModel.objects.filter(username=self.request.user)
      #   print(context['brand'] )
        tab = self.kwargs['hp']
        context['tablet'] = ProductModel.objects.filter(p_brand__brand = tab , p_category__category = 'Tablet')
        print(context['tablet'])
        context['mobile'] = ProductModel.objects.filter(p_category__category = 'MobilePhones')
        return context
    


class MobileView(TemplateView):
    model = ProductModel
    template_name = 'base/mobile.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['feature'] = ProductModel.objects.filter(is_featured = True)
        context['brand'] = BrandModel.objects.all( )
        context['category'] = CategoryModel.objects.all()
        context['cart'] = CartModel.objects.filter(username=self.request.user)
        tab = self.kwargs['brand']
        context['mobile'] = ProductModel.objects.filter(p_brand__brand = tab , p_category__category = 'MobilePhones')
        context['tablet'] = ProductModel.objects.filter(p_category__category = 'Tablet')
        return context
        


class ProductDetailView(DetailView, FormView):
    template_name = 'base/product_detail.html'
    form_class = ReviewForm
    model = ProductModel
    def get_success_url(self):
       id = self.kwargs['pk']
       return reverse_lazy('product_detail', kwargs={'pk': id})
   
    def form_valid(self, form):
       rate = self.request.POST.get('rate')
       event = form.save(commit=False)
       event.username = self.request.user
       event.rating= int(rate)
       event.titleproduct_id= self.kwargs['pk']
       event.save()
       return super().form_valid(form)
       
       
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
       context= super().get_context_data(**kwargs)
       id = self.kwargs['pk']
       rate = self.request.POST.get('rate')
       context['stars'] = rate
       context['category'] = CategoryModel.objects.all()
       context['brand'] = BrandModel.objects.all( )
       context['proddes']=ProductDescriptionModel.objects.get(id=id)
       context['review']= ReviewModel.objects.filter(titleproduct = id)
       context['short']= ProductShortDescriptionModel.objects.filter(productname=id)
       context['images']= ProductImageModel.objects.filter(productid=id)
       context['info']= AdditionalInformationModel.objects.filter(productname=id)
       context['cart'] = CartModel.objects.filter(username=self.request.user)
       
       return context


class AboutView(TemplateView):
   template_name = 'base/about_us.html'

class ContactView(TemplateView):
   template_name = 'base/contact_us.html'

class IndexFixedHeaderView(TemplateView):
   template_name = 'base/index_fixed_header.html'

class AccountView(TemplateView): 
   template_name = 'base/my_account.html'
   def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
      context =  super().get_context_data(**kwargs)
      context['category'] = CategoryModel.objects.all()
      context['brand'] = BrandModel.objects.all( )
      context['cart'] = CartModel.objects.filter(username=self.request.user)
      return context
      


class AddtocartView(View):
#    template_name='base/product_detail.html'
   def get(self, request, product_id):
       user = self.request.user
      #  print('id form cartmodel:', product_id)
       product_id = self.kwargs['product_id']
    #    print(product_id)
      #  print('2nd:', product)
       if CartModel.objects.filter(productid=product_id).exists():
         product = CartModel.objects.get(productid=product_id, username= self.request.user)
         # print('3rd: ',ProductModel.objects.filter(id=product_id))
         product.quantity += 1
         product.save()
       else:
        cart= CartModel(username=user, productid_id=product_id)
        cart.save()
       return redirect('/showcart/', kwargs={'pk': product_id})
   def get_context_data(self, **kwargs) -> dict[str, Any]:
       context = super().get_context_data(**kwargs)
       context['category'] = CategoryModel.objects.all()
       context['brand'] = BrandModel.objects.all( )
       context['cart'] = CartModel.objects.filter(username=self.request.user)
       return context
   
class decreaseformCart(View): 
   def get(self, request, product_id):
      user = self.request.user
      # print(product_id, "user", user)
      
      product = CartModel.objects.get(productid= product_id)
      # print(product)
      if CartModel.objects.filter(productid_id=product_id).exists() and product.quantity >1:
         # print("my+++++",product.total_price)
         product.quantity -= 1
         product.save()
      else:
         product.delete()
      return redirect('/showcart/', kwargs={'pk': product_id})
   def get_context_data(self, **kwargs):
       id = self.kwargs['product_id']
      #  print(id)
       context = super().get_context_data(**kwargs)
       context['category'] = CategoryModel.objects.all()
       context['brand'] = BrandModel.objects.all( )
       context['cart'] = CartModel.objects.filter(username=self.request.user)
       return context

class RemoveFormCart(DeleteView):
   model = CartModel
   success_url = '/showcart/'


   
   

class ShowCartView(TemplateView):
   template_name = 'base/checkout_cart.html'
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      brand = BrandModel.objects.all( )
      cart= CartModel.objects.filter(username=self.request.user)
      category= CategoryModel.objects.all()
      items = CartModel.objects.filter(username=self.request.user)
      if items:
         # total_price= CartModel.objects.filter(username=self.request.user).aggregate(Sum('productid__discounted_price'))
         total_prices= CartModel.objects.filter(username=self.request.user)
         li = []
         abc=None
         for i in total_prices:
            # print(i.quantity* i.productid.discounted_price)
            li.append(i.quantity* i.productid.discounted_price)
            abc = sum(li)
         shipping_charges = 100
         total_with_shipping = abc + shipping_charges
      
      context = {'item':items, 'total_price':abc, 'total_with_shipping':total_with_shipping,
                  'brand':brand, 'cart':cart, 'category':category}
      return context
   
class CheckOutInfoView(FormView):
   template_name = 'base/checkout_info.html'
   form_class = AddressForm
   success_url = '/payment/'
   def form_valid(self, form):
         event = form.save(commit=False)
         event.username = self.request.user
         event.save()
         form.save()
         return super().form_valid(form)
   

class createcheckoutsession(View):
    
   def post(self, *args, **kwargs):
        items= CartModel.objects.filter(username=self.request.user).values()
        for item in items:
            item=item['productid_id']
            
        print(items)
      #   total_price= CartModel.objects.filter(username=self.request.user).aggregate(Sum('productid__discounted_price'))
      #   total_price_s=(total_price['productid__discounted_price__sum'])
        total_prices= CartModel.objects.filter(username=self.request.user)
        li = []
        for i in total_prices:
            # print(i.quantity* i.productid.discounted_price)
            li.append(i.quantity* i.productid.discounted_price)
            abc = sum(li)
        shipping_charges = 100
        total_with_shipping= abc + shipping_charges
        checkout_session = stripe.checkout.Session.create(
           payment_method_types = ['card'],
            line_items=[
                {
                  'price_data':{
                     'currency':'usd',
                     'unit_amount':int(total_with_shipping*100),
                     'product_data':{
                                      
                           'name':item
                     },
                  },
                  'quantity':1
                },
            ],
            mode='payment',
            success_url='http://127.0.0.1:8000/paymentcomplete/',
            # cancel_url='',
        )

        return redirect(checkout_session.url, code=303)



class PaymentView(TemplateView):
    template_name = 'base/checkout_payment.html'


class PaymentCompleteView(TemplateView):
   template_name = 'base/checkout_complete.html'
   def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
      total_price= CartModel.objects.filter(username=self.request.user).aggregate(Sum('productid__discounted_price'))
      total_price_s=(total_price['productid__discounted_price__sum'])
      cart = CartModel.objects.filter(username=self.request.user)
      shipping_charges = 100
      total_with_shipping= total_price_s + shipping_charges
      context= super().get_context_data(**kwargs)
      context={'total_with_shipping': total_with_shipping, 'cart':cart}
      return context

   

      
   
   
       


 
    

