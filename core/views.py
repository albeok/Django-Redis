from django.shortcuts import render
from products.models import Lot
from django.contrib.auth.models import User
from .forms import HashLotModelForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import redis

client = redis.StrictRedis(host='127.0.0.1', port='6379', password="", db=0)

def homepage(request):
    return render(request, "core/homepage.html")

class UserDetailView(DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'core/user_profile.html'

@method_decorator(staff_member_required, name='dispatch')
class UserList(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'core/user_list.html'

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

def track_hash_page(request):
    form = HashLotModelForm
    context = {"form":form}
    return render(request, "core/track_hash_page.html", context)

def track_hash_result(request):
    if request.method == "POST":
        q =request.POST['q']
        hashes = Lot.objects.filter(hash__contains=q)
        return render(request, 'core/track_hash_result.html', {"q": q, "hashes": hashes})
    else:
        return render(request, 'core/track_hash_result.html')

def check_last_ip(request):
    username = request.user.username
    last_ip = client.get(username)
    current_ip = request.META['REMOTE_ADDR']
    if last_ip is None:
        client.set(username, current_ip)
    elif current_ip != last_ip:
        client.set(username, current_ip)
        return HttpResponse("current ip address is different from the previous one")