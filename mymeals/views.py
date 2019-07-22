from django.shortcuts import render

# Create your views here.
from .models import products, category


def meals_list(request):
    product_list = products.objects.filter(published=True).order_by('-pub_date')[:4]
    context      = {
        'product_list' : product_list ,

    }
    return render(request, 'mymeals/index.html', context)




def meals_details(request, slug):
    product_detail = products.objects.get(slug=slug)

    context ={'product_detail' : product_detail,}
    return render(request, 'mymeals/product-single.html', context)



def shop(request):
    product_list = products.objects.filter(published=True).order_by('-pub_date')[:6]
    category_list = category.objects.all()
    context      = {
        'product_list' : product_list ,
        'category_list'     : category_list ,
    }
    return render(request, 'mymeals/shop.html', context)


def about(request):
    context = {}

    return render(request, 'mymeals/about.html', context)


def conntact(request):
    context = {}

    return render(request, 'mymeals/contact.html', context)    
