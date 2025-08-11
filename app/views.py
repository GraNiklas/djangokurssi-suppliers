from django.shortcuts import render, redirect
from .models import Supplier, Product

def landingview(request):
    return render(request, 'landingpage.html')

def productlistview(request):
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

def supplierlistview(request):
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