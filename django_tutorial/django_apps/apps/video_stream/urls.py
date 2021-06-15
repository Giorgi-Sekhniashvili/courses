from django.urls import path
from .views import video_stream_view_back, video_stream_view_front, VideoListView, MainPageView

app_name = 'video_stream'

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page_view'),
    path('video_stream_front', video_stream_view_front, name='video_stream_front'),
    path('video_stream_back', video_stream_view_back, name='video_stream_back'),
    path('video_list/', VideoListView.as_view(), name='video_list_view')
]
