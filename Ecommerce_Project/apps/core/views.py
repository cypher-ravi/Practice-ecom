from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView,DetailView
from .models import *



# Create your views here.
class HomeView(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {
            'categories' : categories
        }
        return render(request, 'index.html',context)
        


class CartView(TemplateView):
    template_name = 'cart.html'
    

class CheckoutView(View):
    def get(self, request):
        return render(request, 'checkout.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')