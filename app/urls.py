from django.urls import path

from .views import addproduct, confirmdeleteproduct, deleteproduct, edit_product_get, edit_product_post, edit_supplier_get, edit_supplier_post, landingview, login_action, loginview, logout_action, productlistview, productsfiltered, searchsuppliers, supplierlistview, addsupplier, deletesupplier,confirmdeletesupplier

urlpatterns= [
	path('landing/',landingview),
	path('',loginview),
	path('login/',login_action),
	path('logout/',logout_action),


	# products
	path('products/',productlistview),
	path('add-product/',addproduct),
	path('delete-product/<int:id>',deleteproduct),
	path('confirm-delete-product/<int:id>',confirmdeleteproduct),
	path('edit-product-get/<int:id>',edit_product_get),
	path('edit-product-post/<int:id>/',edit_product_post),
	path('products-by-supplier/<int:id>/',productsfiltered),


	# suppliers
	path('suppliers/',supplierlistview),
	path('add-supplier/',addsupplier),
	path('delete-supplier/<int:id>',deletesupplier),
	path('confirm-delete-supplier/<int:id>',confirmdeletesupplier),
	path('search-suppliers/',searchsuppliers),
	path('edit-supplier-get/<int:id>/',edit_supplier_get),
	path('edit-supplier-post/<int:id>/',edit_supplier_post)
]