from django.shortcuts import render, redirect
from .models import Car, Seller
from .forms import CarForm, SellerForm

def seller_list(request):
    sellers = Seller.objects.all()
    return render(request, 'seller_list.html', {'sellers': sellers})

def seller_detail(request, id):
    seller = Seller.objects.get(id = id)
    return render(request, 'seller_detail.html', {'seller': seller})

def seller_create(response):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid:
            seller = form.save()
            return redirect('seller_detail', id = seller.id)
    else:
        form = SellerForm()
        return render(request, 'seller_form.html', {'form': form})

def seller_update(request, id):
    seller = Seller.objects.get(id = id)
    if request.method == 'POST':
        form = SellerForm(request.POST, instance = seller)
        if form.is_valid:
            seller = form.save()
            return redirect('seller_detail', id = seller.id)
    else:
        form = SellerForm(instance = seller)
        return render(request, 'seller_form.html', {'form': form})

def seller_delete(request, id):
    if request.method == 'POST':
        Seller.objects.get(id = id).delete()
    return redirect('seller_list')

def car_list(request):
<<<<<<< HEAD
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})

def car_detail(request, id):
    car = Car.objects.get(id = id)
    return render(request, 'car_detail.html', {'car': car})

def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid:
            car = form.save()
            return redirect('car_detail', id = car.id)
    else:
        form = CarForm()
        return render(request, 'car_form.html', {'form': form})

def car_update(request, id):
    car = Car.objects.get(id = id)
    if request.method == 'POST':
        form = CarForm(request.body, instance = car)
        if form.is_valid:
            car = form.save()
            return redirect('car_detail', id = car.id)
    else:
        form = CarForm(instance = car)
        return render(request, 'car_form.html', {'form': form})

def car_delete(request, id):
    if request.method == 'POST':
        Car.objects.get(id = id).delete()
    return redirect('car_list')
=======
    car = Car.objects.all()
    return render(request, 'car_list.html', {'car': car})
>>>>>>> mike
