from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('showall/<str:p_brand>/', views.ShowAllView.as_view(), name='showall'),
    # path('showall/<str:p_category>/', views.ShowAllView.as_view(), name='showall'),
    # path('product/', views.ProductView.as_view(), name= 'product'),
    path('mobile/<str:brand>/', views.MobileView.as_view(), name='mobile'),

    # path('apple/', views.AppleView.as_view(), name='apple'),
    # path('microsoft/', views.MicrosoftView.as_view(), name='microsoft'),
    # path('samsung/', views.SamsungView.as_view(), name='samsung'),

    path('tab/<str:hp>/', views.TabletView.as_view(), name='tab'),
    path('tab/<str:apple>/', views.TabletView.as_view(), name='tab'),
    path('tab/<str:samsung>/', views.TabletView.as_view(), name='tab'),

    path('product_detail/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),


    path('contact/', views.ContactView.as_view(), name='contact'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('indexfixedheader/', views.IndexFixedHeaderView.as_view(), name='indexfixedheader'),

    path('accountp/', views.AccountView.as_view(), name='accountp'),
    # path('createuser/', views..as_view(), name='account'),

    path('addtocart/<int:product_id>/', login_required(views.AddtocartView.as_view()), name='addtocart'),
    path('removefromcart/<int:product_id>/', login_required(views.RemoveformCart.as_view()), name='removefromcart'),
    path('showcart/', login_required(views.ShowCartView.as_view()), name='showcart'),
    path('checkoutinfo/', login_required(views.CheckOutInfoView.as_view()), name='checkoutinfo'),
    path('payment/', login_required(views.PaymentView.as_view()), name='payment'),
    path('createcheckoutsession/', login_required(views.createcheckoutsession.as_view()), name='createcheckoutsession'),
    path('paymentcomplete/', login_required(views.PaymentCompleteView.as_view()), name='paymentcomplete'),



    
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

