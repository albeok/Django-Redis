from urllib import request
from django.shortcuts import render
from .models import Product
from django.shortcuts import HttpResponseRedirect
def product_view(request):
    if request.method == "POST":
        form = Product(request.POST)
        if form.is_valid():
            name_product = form.cleaned_data['name_product']
            description = form.cleaned_data['description']
            tx_id = form.cleaned_data['tx_id']
            return HttpResponseRedirect("/")
    else:
        form = Product()
    context = {'form':form}
    return render(request, 'registration/product_registration.html', context)
