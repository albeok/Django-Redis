from multiprocessing import context
from urllib import request
from django.shortcuts import get_object_or_404, render
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.views.generic import View, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# from .forms import LotModelForm
from .models import Lot
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic.edit import CreateView
from django.shortcuts import HttpResponseRedirect

class LotRegistrationCreateView(LoginRequiredMixin, CreateView):
    model = Lot
    fields = ["lot_code", "tracking_code", "product", "production_quantity", "date_time_arrival", "date_time_production", "manufacturing_plant", "recipient"]
    template_name = "products/lot_registration.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

# def lot_detail_view(request, pk):
#     lot = get_object_or_404(Lot, pk=pk)
#     context = {"lot": lot}
#     return render("/products/lot_detail.html", context)


# # def ProductRegistrationView(request):
# #     if request.method == "POST":
# #         form = ProductsModelForm(request.POST)
# #         if form.is_valid():
# #             name_product = form.cleaned_data['name_product']
# #             image = form.cleaned_data['image']
# #             lot_code = form.cleaned_data['lot_code']
# #             tracking_code = form.cleaned_data['tracking_code']
# #             Product.objects.create(name_product=name_product, image=image, lot_code=lot_code, tracking_code=tracking_code)
# #             Product.save()
# #             return HttpResponseRedirect("/")
# #     else:
# #         form = ProductsModelForm()
# #     context = {"form": form}
# #     return render(request, 'products/product_registration.html', context)

# def lot_registration_view(request):
#     if request.method == "POST":
#         form = LotModelForm(request.POST)
#         if form.is_valid():
#             new_lot = form.save()
#             print("new_lot:" , new_lot)
#             return HttpResponse("Lot creato con successo")
#     else:
#         form = LotModelForm()
#     context = {"form": form}
#     return render(request, 'products/lot_registration.html', context)

def lot_detail_view(request, pk):
    lot = get_object_or_404(Lot, pk=pk)
    context ={"lot": lot}
    return render(request, "products/lot_detail.html", context)


# def track_product(self):
#     products_list = TrackingCode.objects.filter()
#     return self.fields
