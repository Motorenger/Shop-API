from django.urls import path

from products.views import ProductListView, ProductRetrieveView


app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<int:pk>/', ProductRetrieveView.as_view(), name='retrieve')
]
