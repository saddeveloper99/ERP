from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Inbound, Outbound
from decimal import Decimal


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
            return redirect('/login')

    elif request.method == 'POST':
        user = request.user
        code = request.POST.get('code', '')
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        price = request.POST.get('price', '')
        sizes = request.POST.get('size', '')
        if code == '' or name == '' or sizes == '' or price == '':
            return render(request, 'erp/product_list.html', {'error': '빈칸을 입력해 주세요.'})
        else:
            product = Product.objects.create(
                user=user,
                code=code,
                name=name,
                description=description,
                price=price,
                size=sizes           
                )
            product.save()
            return redirect('/product_list')
    

# return render(request, 'erp/inbound_create.html')

@login_required
def inbound_create(request):
    product = Product.objects.all()

    if request.method == 'GET':
        return render(request, 'erp/inbound_create.html', {'product_list':product})

    elif request.method == 'POST':
        product_code = request.POST.get('product_code')
        inbound_quantity = request.POST.get('inbound_quantity', '')

        product = Product.objects.get(code=product_code)

        if inbound_quantity == '':
            return render(request, 'erp/inbound_create.html', {'product_list':product, 'error': '수량을 입력해 주세요.'})
       
        else:     
            Inbound.objects.create(
                product = product,
                inbound_quantity = inbound_quantity,
                amount= product.price * Decimal(inbound_quantity)
            )
            return redirect('/product_list')
    

def outbound_create(request):
    product = Product.objects.all()

    if request.method == 'GET':
        return render(request, 'erp/outbound_create.html', {'product_list':product})

    elif request.method == 'POST':
        product_code = request.POST.get('product_code')
        outbound_quantity = request.POST.get('outbound_quantity', '')

        product = Product.objects.get(code=product_code)

        if outbound_quantity == '':
            return render(request, 'erp/outbound_create.html', {'product_list':product, 'error': '수량을 입력해 주세요.'})
        elif int(outbound_quantity) > int(product.quantity):
            return render(request, 'erp/outbound_create.html', {'product_list':product, 'error': '출고 수량이 현재 재고량보다 많습니다.'})
        else:     
            Outbound.objects.create(
                product = product,
                outbound_quantity = outbound_quantity,
                amount= product.price * Decimal(outbound_quantity)
            )
            return redirect('/product_list')