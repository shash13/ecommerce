from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import ListView
from .models import Product

# Create your views here.

def homepage(request):
    context={
        'title':'Homepage',
        'content': "This is Homepage"
    }

    return  render(request,'shop/homepage.html',context)


def index(request):
    context = {
        'title': 'Index',
        'content': "This is Index Page"
    }

    return render(request, 'shop/index.html', context)


def contact(request):
    form = ContactForm()
    context = {
        'title': 'Contact',
        'content': "This is Contact Page",
        'form': form,
    }

    return render(request, 'shop/contact.html', context)


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "shop/list.html"


def product_list_view(request):
    context = {
        'object_list': Product.objects.all(),
    }
    return render(request, "shop/list.html", context)


def product_detail_view(request,pk):
    context = {
        'object_list': Product.objects.get(pk=pk),
    }
    return render(request, "shop/detail.html", context)
