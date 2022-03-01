from django.urls import path
from . import views

# URL configurattion

urlpatterns = [
    #path('hello/', views.oneProduct)
    #path('hello/<int:id/', views.oneProduct),
    # path('<int:id>/', views.oneProduct, name= 'product'), 
    # path('', views.products, name = 'products'),
    path('table', views.viewProducts,),
    # path('inventory', views.reduceInventory,),
    
]