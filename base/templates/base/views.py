from typing import Any
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import ProductModel, CategoryModel, CustomerModel
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import (CustomerRegisterationForm, LoginForm, MyPasswordChangeForm, 
                    MyPasswordResetForm, MySetPasswordForm)
from django.contrib.auth.views import (LoginView, PasswordChangeView, LogoutView, 
                                       PasswordChangeDoneView, PasswordResetView,
                                       PasswordResetDoneView, PasswordResetConfirmView,
                                       PasswordResetCompleteView)



# Create your views here.


# This View is for Dashboard/Home

class IndexView(TemplateView):
    model = ProductModel
    template_name = "base/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feature'] = ProductModel.objects.filter(is_featured = True)
        context['mobile'] = ProductModel.objects.filter(p_category__category = 'MobilePhones')
        context['tablet'] = ProductModel.objects.filter(p_category__category = 'Tablet')
        return context

class AppleView(TemplateView):
    model = ProductModel
    template_name = 'base/apple.html'
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['feature'] = ProductModel.objects.filter(is_featured = True)
        context['apple'] = ProductModel.objects.filter(p_brand__brand = 'Apple' , p_category__category = 'MobilePhones')
        context['tablet'] = ProductModel.objects.filter(p_category__category = 'Tablet')
        return context
    
class SamsungView(TemplateView):
    model = ProductModel
    template_name = 'base/samsung.html'
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['feature'] = ProductModel.objects.filter(is_featured = True)
        context['samsung'] = ProductModel.objects.filter(p_brand__brand = 'Samsung' , p_category__category = 'MobilePhones')
        context['tablet'] = ProductModel.objects.filter(p_category__category = 'Tablet')
        return context
    
class MicrosoftView(TemplateView):
    model = ProductModel
    template_name = 'base/microsoft.html'
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['feature'] = ProductModel.objects.filter(is_featured = True)
        context['microsoft'] = ProductModel.objects.filter(p_brand__brand = 'Microsoft' , p_category__category = 'MobilePhones')
        context['tablet'] = ProductModel.objects.filter(p_category__category = 'Tablet')
        return context
    

class TabletView(TemplateView):
    model = ProductModel
    template_name = 'base/tablet.html'


    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['feature'] = ProductModel.objects.filter(is_featured = True)
        tab = self.kwargs['hp']
        # print(tab)
        if tab == 'samsung':
         context['tablet'] = ProductModel.objects.filter(p_brand__brand = 'Samsung' , p_category__category = 'Tablet')
        elif tab == 'hp' :
         context['tablet'] = ProductModel.objects.filter(p_brand__brand = 'HP' , p_category__category = 'Tablet')
        elif tab == 'apple':
         context['tablet'] = ProductModel.objects.filter(p_brand__brand = 'Apple' , p_category__category = 'Tablet')
        context['mobile'] = ProductModel.objects.filter(p_category__category = 'MobilePhones')
        return context
        


# class ProductView(TemplateView):
#     template_name = "base/product.html"

class ProductDetailView(DetailView):
    template_name = 'base/product_detail.html'
    model = ProductModel

class AboutView(TemplateView):
   template_name = 'base/about_us.html'

class ContactView(TemplateView):
   template_name = 'base/contact_us.html'

class IndexFixedHeaderView(TemplateView):
   template_name = 'base/index_fixed_header.html'

class AccountView(TemplateView):
   template_name = 'base/my_account.html'

# class CustomerUserView(CreateView):
#    model = User
#    fields = '__all__'
#    template_name = 'base/userform.html'
    

class MyLoginView(LoginView):
  form_class = LoginForm
  template_name = 'app/login.html'
  success_url = '/profile/'

class MyLogoutView(LogoutView):
 next_page = '/login/'
 
class MyPasswordChangeView(PasswordChangeView):
 template_name = 'app/changepassword.html'
 form_class = MyPasswordChangeForm
 success_url = '/passwordchangedone/'

 def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Password changed successfully.')
        return response
 
class MyPasswordChangeDoneView(PasswordChangeDoneView):
 template_name = 'app/passwordchangedone.html'

class MyPasswordResetView(PasswordResetView):
 template_name = 'app/passwordreset.html'
 form_class = MyPasswordResetForm


class MyPasswordResetDoneView(PasswordResetDoneView):
 template_name = 'app/passwordresetdone.html'

class MyPasswordResetConfirmView(PasswordResetConfirmView):
 template_name = 'app/passwordresetconfirm.html'
 form_class = MySetPasswordForm

class MyPasswordResetCompleteView(PasswordResetCompleteView):
 template_name = 'app/passwordresetcomplete.html'