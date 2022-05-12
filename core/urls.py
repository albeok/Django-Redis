from django.urls import path
from .views import homepage, search_tracking_code, LotDetailView, track_lot
urlpatterns = [
    path("", homepage, name="homepage"),
    path("search/", search_tracking_code, name="search_tracking_code"),
    path("lot_detail/<int:pk>/", LotDetailView.as_view(), name="lot_detail"),
    path("track_product/", track_lot, name="track_lot"),
]