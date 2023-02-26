from django.urls import path
from api import views
urlpatterns = [
    path('Productsapi',views.ProductsView.as_view(),name="Product_view"),
    path('Product_details_api/<int:item_id>',views.PrductView.as_view(),name="Product_Details__view"),


    
   
]
