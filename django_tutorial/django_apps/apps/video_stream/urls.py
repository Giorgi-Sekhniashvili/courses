from django.urls import path
from .views import video_stream_view_back, video_stream_view_front

app_name = 'video_stream'

urlpatterns = [
    path('', video_stream_view_front, name='video_stream_front'),
    path('video_stream_back', video_stream_view_back, name='video_stream_back')
]
