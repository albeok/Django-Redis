from django.urls import path
from .views import LotRegistrationCreateView
urlpatterns = [
    path("registration/", LotRegistrationCreateView.as_view(), name="lot_registration"),

]