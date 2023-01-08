from django.urls import path
from . import views

urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('register/',views.register.as_view(),name='register'),
    path('log_in/',views.log_in.as_view(),name='log_in'),
    path('l_out/',views.l_out.as_view(),name='l_out'),
    path('all_products/',views.all_products.as_view(),name='all_products'),
    path('display_products/<str:category_name>',views.display_products.as_view(),name='display_products'),
    path('view_product/<int:pk>',views.view_product.as_view(),name='view_product'),
]