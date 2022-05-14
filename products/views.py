from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Lot

class LotRegistrationCreateView(LoginRequiredMixin, CreateView):
    model = Lot
    fields = ["lot_code", "tracking_code", "product", "production_quantity", "date_time_arrival", "date_time_production", "manufacturing_plant", "recipient"]
    template_name = "products/lot_registration.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
