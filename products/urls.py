from django.urls import path, include

from products import views

urlpatterns = [

    path('latest-products/', views.LatestProductList.as_view(), name='latest-products'),
    path('products/search/', views.search, name='search-products'),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
]