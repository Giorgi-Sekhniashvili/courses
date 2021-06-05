from django.urls import path
from .views import video_stream_view, video_stream_view_front, video_stream_view_2

app_name = 'video_stream'

urlpatterns = [
    path('', video_stream_view_front, name='video_stream_front'),
    path('vidoe_stream_2', video_stream_view_2, name='video_stream_2'),
    path('video_stream', video_stream_view, name='video_stream')
]
