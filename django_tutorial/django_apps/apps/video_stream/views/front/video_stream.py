from django.shortcuts import render


def video_stream_view_front(request):
    return render(request, 'video_stream/video_stream.html')
