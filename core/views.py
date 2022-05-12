from django.shortcuts import redirect, render
from products.models import Lot
from django.views.generic import View, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

def homepage(request):
    return render(request, "core/homepage.html")

def search_tracking_code(request):
    if request.method == "POST":
        searched =request.POST['searched']
        lots = Lot.objects.filter(tracking_code__contains=searched)
        return render(request, 'core/search_tracking_code.html', {"searched": searched, "lots": lots})
    else:
        return render(request, 'core/search_tracking_code.html')

class LotDetailView(LoginRequiredMixin, DetailView):
    template_name = "core/lot_detail.html"
    model = Lot

class TrackProductView(View):
    pass

def track_lot(request):
    if request.method == "POST":
        q =request.POST['q']
        lots = Lot.objects.filter(hash__contains=q)
        return render(request, 'core/track_lot.html', {"searched": q, "lots": lots})
    else:
        return render(request, 'core/search_tracking_code.html')