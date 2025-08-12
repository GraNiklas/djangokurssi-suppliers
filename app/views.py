from math import prod
from django.shortcuts import render, redirect
from .models import Supplier, Product
from django.contrib.auth import authenticate,login,logout

#LANDING
def landingview(request):
    return render(request, 'landingpage.html')

#LOGIN
def loginview(request):
    return render(request, 'loginpage.html')

def login_action(request):
    usern = request.POST['username']
    passw = request.POST['password']
    user = authenticate(username = usern,password = passw)
    if user:
        login(request,user)
        context = {'name':user}
        return render(request,'landingpage.html',context)
    else:
        return render(request,'loginerror.html')

def logout_action(request):
    logout(request)
    return render(request,'loginpage.html')


#PRODUCT
def productlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    productlist = Product.objects.all()
    supplierlist = Supplier.objects.all()
    context = {'products': productlist ,'suppliers':supplierlist}
    return render(request, 'productlist.html',context)

def addproduct(request):
    a = request.POST['productname']
    b = request.POST['price']
    c = request.POST['stock']
    d = request.POST['supplier']
    Product(productname = a, price = b, stock = c, supplier = Supplier.objects.get(id = d)).save()
    return redirect(request.META['HTTP_REFERER'])


def confirmdeleteproduct(request,id):
    product = Product.objects.get(id = id)
    context = {'product': product}
    return render(request,"confirmdeleteprod.html",context)

def deleteproduct(request,id):
    Product.objects.get(id=id).delete()
    return redirect(productlistview)

def edit_product_get(request,id):
    product = Product.objects.get(id=id)
    context =  {'product': product}
    return render(request,"editprod.html",context)

def edit_product_post(request,id):
    product = Product.objects.get(id=id)
    product.price = request.POST['price']
    product.stock = request.POST['stock']
    product.save()
    return redirect(productlistview)




#SUPPLIER
def supplierlistview(request):
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    supplierlist = Supplier.objects.all()
    context = {'suppliers': supplierlist}
    return render(request, 'supplierlist.html',context)

def addsupplier(request):
    a = request.POST['companyname']
    b = request.POST['contactname']
    c = request.POST['address']
    d = request.POST['phone']
    e = request.POST['email']
    f = request.POST['country']
    Supplier(companyname = a, contactname = b, address = c,phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])

def confirmdeletesupplier(request,id):
    supplier = Supplier.objects.get(id = id)
    context = {'supplier': supplier}
    return render(request,"confirmdeletesupp.html",context)

def deletesupplier(request,id):
    Supplier.objects.get(id=id).delete()
    return redirect(supplierlistview)

def searchsuppliers(request):
    search = request.POST['search']
    filtered = Supplier.objects.filter(companyname__icontains=search)
    context = {'suppliers':filtered}
    return render(request,"supplierlist.html",context)


def productsfiltered(request,id):
    products = Product.objects.all()
    filtered = products.filter(supplier = id)
    context = {'products': filtered}
    return render(request,"productlist.html",context)

def edit_supplier_get(request,id):
    supplier = Supplier.objects.get(id=id)
    context =  {'supplier': supplier}
    return render(request,"editsupp.html",context)

def edit_supplier_post(request,id):
    supplier = Supplier.objects.get(id=id)
    supplier.companyname = request.POST['companyname']
    supplier.contactname = request.POST['contactname']
    supplier.address = request.POST['address']
    supplier.phone = request.POST['phone']
    supplier.email = request.POST['email']
    supplier.country = request.POST['country']
    supplier.save()
    return redirect(supplierlistview)

