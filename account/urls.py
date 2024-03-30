from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('customer_registeration/', views.CustomerRegisterationView.as_view(), name='customer_registeration'),

    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', login_required(views.MyLogoutView.as_view()), name='logout'),
    path('changepassword/', login_required(views.MyPasswordChangeView.as_view()), name='changepassword'),
    path('passwordchangedone/', login_required(views.MyPasswordChangeDoneView.as_view()), name='passwordchangedone'),
    path('passwordreset/', views.MyPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', login_required(views.MyPasswordResetDoneView.as_view()), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', login_required(views.MyPasswordResetConfirmView.as_view()), name='password_reset_confirm'),
    path('password_reset_complete/', login_required(views.MyPasswordResetCompleteView.as_view()), name='password_reset_complete'),

]
