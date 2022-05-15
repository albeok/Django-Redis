from django.urls import path
from .views import homepage, UserDetailView, UserList, search_tracking_code, LotDetailView, track_hash_page, track_hash_result
urlpatterns = [
    path("", homepage, name="homepage"),
    path("user/<int:pk>/", UserDetailView.as_view(), name="user_profile"),
    path("user_list/", UserList.as_view(), name="user_list"),
    path("search/", search_tracking_code, name="search_tracking_code"),
    path("lot_detail/<int:pk>/", LotDetailView.as_view(), name="lot_detail"),
    path("track_hash_page/", track_hash_page, name="track_hash_page"),
    path("track_hash_result/", track_hash_result, name="track_hash_result"),
]