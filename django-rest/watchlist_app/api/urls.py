from django.urls import include, path
from watchlist_app.api.views import WatchDetailAV, WatchListAV, StreamPlatformAV, StreamDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie_list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie_detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>', StreamDetailAV.as_view(), name='stream_detail'),
]