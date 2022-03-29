from django.urls import path
from main_app import views

urlpatterns = [
    path('api/products/',views.ProductApi.as_view(),name='Product_list_api'),
    path('api/products/<int:pk>',views.ProductApi.as_view(),name='Product_retrieve_api'),
    path('api/category/',views.CategoryApi.as_view(),name='Category_list_api'),
    path('api/category/<int:pk>',views.CategoryApi.as_view(),name='Category_list_api'),


]
