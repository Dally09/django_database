from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404

from myapp.forms import ProductForm
from myapp.models import Product


# Create your views here.
@login_required
def home(request):
    products = Product.objects.all() # select * from products
    for product in products:
        print(product.name, product.code, product.price, product.cost, product.category)
    return render(request, 'home.html', {'products': products})

@login_required
def add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'{form.cleaned_data["name"]} successfully added')
            # messages.error(request, f'{form.cleaned_data["name"]} failed to add')
            return redirect('home')
    else:
        form = ProductForm()

    # Product.objects.create(name="Unga",
    #                        code="01008998",
    #                        price=510.0,
    #                        cost=488.0,
    #                        category="Foods",
    #                        for_sale=False)
    # Product.objects.create(name="Lemon",
    #                        code="01008972",
    #                        price=50.0,
    #                        cost=48.0,
    #                        category="Foods",)
    # Product.objects.create(name="Onion",
    #                        code="01008901",
    #                        price=10.0,
    #                        cost=8.0,
    #                        category="Foods",)
    return render(request, 'add.html', {'form': form})


@login_required
def delete_product(request, id):
    product = Product.objects.get(id=id) #select * from products where id=65
    product.delete() # delete * from products where id=65
    messages.warning(request, f'{product.name} successfully deleted')
    return redirect('home')


@login_required
def edit_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.Files, instance=product) # req files throws an error
        if form.is_valid():
            form.save()
            messages.success(request, f'{product.name} successfully updated')
            # messages.error(request, f'{product.name} failed to update')
            return redirect('home')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit.html', {'form': form})


@login_required
def details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'details.html', {'product': product})


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request,f"{user} successfully logged in")
            return redirect('home')
        else:
            form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def signup(request):
    return None

@login_required
def signout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')