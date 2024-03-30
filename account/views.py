from django.shortcuts import render
from django.contrib import messages
from django.views.generic.edit import FormView
from .forms import (CustomerRegisterationForm, LoginForm, MyPasswordChangeForm, 
                    MyPasswordResetForm, MySetPasswordForm)
from django.contrib.auth.views import (LoginView, PasswordChangeView, LogoutView, 
                                       PasswordChangeDoneView, PasswordResetView,
                                       PasswordResetDoneView, PasswordResetConfirmView,
                                       PasswordResetCompleteView)


# Create your views here.
class CustomerRegisterationView(FormView):
 form_class = CustomerRegisterationForm
 template_name = 'account/customerregistration.html'
 success_url = 'account/customer_registration/'
 def form_valid(self, form):
  form.save()
  messages.success(self.request, "Profile Registered Successfully!!")
  return super().form_valid(form)




class MyLoginView(LoginView):
  form_class = LoginForm
  template_name = 'account/login.html'
  success_url = '/index/'

class MyLogoutView(LogoutView):
 next_page='/account/login/'
#  template_name = 'account/login.html'
 
class MyPasswordChangeView(PasswordChangeView):
 template_name = 'account/changepassword.html'
 form_class = MyPasswordChangeForm
 success_url = '/account/passwordchangedone/'

 def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Password changed successfully.')
        return response
 
class MyPasswordChangeDoneView(PasswordChangeDoneView):
 template_name = 'account/passwordchangedone.html'

class MyPasswordResetView(PasswordResetView):
 template_name = 'account/passwordreset.html'
 form_class = MyPasswordResetForm


class MyPasswordResetDoneView(PasswordResetDoneView):
 template_name = 'account/passwordresetdone.html'

class MyPasswordResetConfirmView(PasswordResetConfirmView):
 template_name = 'account/passwordresetconfirm.html'
 form_class = MySetPasswordForm

class MyPasswordResetCompleteView(PasswordResetCompleteView):
 template_name = 'account/passwordresetcomplete.html'