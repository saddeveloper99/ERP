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
            product_list = Product.objects.all()
            return render(request, 'erp/product_list.html', {'product_list': product_list})
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
            return redirect('/product_list')
    

# return render(request, 'erp/inbound_create.html')

@login_required
def inbound_create(request):
    product_list = Product.objects.all()

    if request.method == 'GET':
        return render(request, 'erp/inbound_create.html', {'product_list':product_list})

    elif request.method == 'POST':
        product_code = request.POST.get('product_code')
        inbound_quantity = request.POST.get('inbound_quantity', '')
        if product_code == '상품 코드':
            return render(request, 'erp/outbound_create.html', {'error': '상품을 선택해주세요', 'product_list':product_list})
        
        product = Product.objects.get(code=product_code)

        if inbound_quantity == '':
            return render(request, 'erp/inbound_create.html', {'error': '수량을 입력해 주세요.','product_list':product_list})
       
        else:     
            Inbound.objects.create(
                product = product,
                inbound_quantity = inbound_quantity,
                amount= product.price * Decimal(inbound_quantity)
            )
            return redirect('/product_list')
    

def outbound_create(request):
    product_list = Product.objects.all()

    if request.method == 'GET':
        return render(request, 'erp/outbound_create.html', {'product_list':product_list})

    elif request.method == 'POST':
        product_code = request.POST.get('product_code')
        outbound_quantity = request.POST.get('outbound_quantity', '')
        if product_code == '상품 코드':
            return render(request, 'erp/outbound_create.html', {'error': '상품을 선택해주세요', 'product_list':product_list})
        
        product = Product.objects.get(code=product_code)

       
        if outbound_quantity == '':
            return render(request, 'erp/outbound_create.html', {'error': '수량을 입력해 주세요.', 'product_list':product_list})
        elif int(outbound_quantity) > int(product.quantity):
            return render(request, 'erp/outbound_create.html', {'error': '출고 수량이 현재 재고량보다 많습니다.', 'product_list':product_list})
        else:     
            Outbound.objects.create(
                product = product,
                outbound_quantity = outbound_quantity,
                amount= product.price * Decimal(outbound_quantity)
            )
            return redirect('/product_list')