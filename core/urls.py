from django.urls import path
from .views import homepage, search_tracking_code, LotDetailView, track_hash_page, track_hash_result
urlpatterns = [
    path("", homepage, name="homepage"),
    path("search/", search_tracking_code, name="search_tracking_code"),
    path("lot_detail/<int:pk>/", LotDetailView.as_view(), name="lot_detail"),
    path("track_hash_page/", track_hash_page, name="track_hash_page"),
    path("track_hash_result/", track_hash_result, name="track_hash_result"),
]