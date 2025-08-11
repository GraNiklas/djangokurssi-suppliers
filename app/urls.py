from django.urls import path

from .views import addproduct, landingview, productlistview, supplierlistview, addsupplier

urlpatterns= [
	path('',landingview),

	path('products/',productlistview),
	path('add-product/',addproduct),

	path('suppliers/',supplierlistview),
	path('add-supplier/',addsupplier),

	
]