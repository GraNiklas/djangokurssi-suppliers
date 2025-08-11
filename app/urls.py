from django.urls import path

from .views import landingview, productlistview, supplierlistview

urlpatterns= [
	path('',landingview),
	path('suppliers/',supplierlistview),
	path('products/',productlistview),
]