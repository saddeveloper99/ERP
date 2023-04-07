from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Inbound, Outbound


# Create your views here.
def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/product_list')
    else:
        return redirect('/login')

@login_required
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
        if code == '' or name == '' or size == '' or price == '' or description == '':
            return render(request, 'erp/product_list.html', {'error': '빈칸을 입력해 주세요.'})
        
        my_product = Product.objects.create(
            name=name,
            code=code,
            description=description,
            price=price,
            size=size 
            )
        my_product.save()
        return redirect('/product_list')
    
