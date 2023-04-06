from django.shortcuts import render, redirect
from .models import Product
# Create your views here.
def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/product_list')
    else:
        return redirect('/login')
    
def product_list_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            all_product = Product.objects.all()
            return render(request, 'erp/product_list.html', {'all_product': all_product})
        else:
            return redirect('/sign-in')

    elif request.method == 'POST':
        name = request.POST.get('name', '')
        code = request.POST.get('code', '')
        description = request.POST.get('description', '')
        price = request.POST.get('price', '')
        size = request.POST.get('size', '')

        my_product = Product.objects.create(
            name=name,
            code=code,
            description=description,
            price=price,
            size=size 
            )
        my_product.save()
        return redirect('/product_list')