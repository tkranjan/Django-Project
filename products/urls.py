from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
    path('product/<int:pk>/',views.ProductDetailView.as_view(),name='product_detail'),
    path('product/create/', views.ProductCreateView.as_view(),name='product_create')
]