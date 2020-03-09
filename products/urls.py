
from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_product, name='create'),
    path('<int:product_id>', views.product_detail, name='detail')
]
