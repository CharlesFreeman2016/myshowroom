from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product


def home(request):
    return render(request, 'shop/home.html')


class ProductsListView(ListView):
    queryset = Product.objects.all()
    template_name = 'shop/products.html'

    #def get_context_data(self, *args, **kwargs):
      #  context = super(ProductsListView, self).get_context_data(*args, **kwargs)
     #   return context

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'shop/products.html', context)
