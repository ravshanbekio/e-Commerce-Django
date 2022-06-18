from django.shortcuts import render, redirect
from django.views import View

from product.models import Capital, Recommended, Product, Category
from base.models import Contact

class DashboardView(View):
    def get(self, request):
        if request.user.is_authenticated:
            capitals = Capital.objects.all()
            recommended_products = Recommended.objects.all()
            products = Product.objects.all()
            home_appliances = Product.objects.filter(product_category=2)
            context = {
                'capitals':capitals,
                'recommended_products':recommended_products,
                'products':products,
                'home_appliances':home_appliances,
            }
            return render(request, 'index.html', context)
        else:
            return redirect('register')

    def post(self, request):
        contact = Contact.objects.create(
            client=request.user,
            message=request.POST['message']
        )
        return redirect('dashboard')

class AboutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'about_we.html')
        else:
            return redirect('register')

    def post(self, request):
        contact = Contact.objects.create(
            client=request.user,
            message=request.POST['message']
        )
        return redirect('dashboard')

class DeliveryView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'dostavka.html')
        else:
            return redirect('register')

    def post(self, request):
        contact = Contact.objects.create(
            client=request.user,
            message=request.POST['message']
        )
        return redirect('dashboard')

class LocationView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'location.html')
        else:
            return redirect('register')

    def post(self, request):
        contact = Contact.objects.create(
            client=request.user,
            message=request.POST['message']
        )
        return redirect('dashboard')

class ProductDetailView(View):
    def get(self, request, category, title):
        if request.user.is_authenticated:
            category = Category.objects.get(category_name=category)
            get_product = Product.objects.get(product_title=title)
            get_products = Product.objects.filter(product_title=title)
            context = {
                'get_product':get_product
            }
            return render(request, 'product_window.html', context)
        return redirect('register')