from django.shortcuts import render, redirect
from django.views import View

from base.models import Contact
from product.models import Box, Category, Product

class BuyProductView(View):
    def get(self, request):
        if request.user.is_authenticated:
            get_box = Box.objects.filter(buyer=request.user)
            context = {
                'get_box':get_box
            }
            return render(request, 'buy_product.html', context)
        return redirect('register')

    def post(self, request):
        contact = Contact.objects.create(
            client=request.user,
            message=request.POST['message']
        )
        return redirect('dashboard')

class AddtoBoxView(View):
    def get(self,request, category, title):
        if request.user.is_authenticated:
            category = Category.objects.get(category_name=category)
            get_product = Product.objects.get(product_title=title)
            to_box = Box.objects.create(
                buyer=request.user,
                product=get_product
            )
            return redirect('box')
        else:
            return redirect('register')