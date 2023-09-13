from django.urls import path

from . import views

urlpatterns = [
	
	path('', views.catas_list, name="catas_list"),
    path('<slug:slug>/', views.cata_details, name='cata_details'),
    path('create-cata', views.cata_create, name='cata_create'),

    
	
	#path('cart/', views.cart, name="cart"),
	#path('checkout/', views.checkout, name="checkout"),

    
    
    #path('update_item/', views.updateItem, name="update_item"),
	#path('process_order/', views.processOrder, name="process_order"),
] 