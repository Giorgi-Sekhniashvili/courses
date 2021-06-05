import threading

import cv2
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators import gzip


# Create your views here.
def video_stream_view_front(request):
    return render(request, 'video_stream/video_stream.html', )


@gzip.gzip_page
def video_stream_view(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(cam.update(), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    return HttpResponse('holaa from my_view')


@gzip.gzip_page
def video_stream_view_2(request):
    try:
        cam = VideoCamera(r'C:\Users\gsekhniashvili\Desktop\10.mp4')
        return StreamingHttpResponse(cam.update(), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    return HttpResponse('holaa from my_view')


class VideoCamera(object):
    def __init__(self, name=None):
        self.video = cv2.VideoCapture(name or 0)
        self.grabbed, self.frame = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()
            frame = self.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield {"first": (b'--frame\r\n'
                         b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n'), "second": (b'--frame\r\n'
                                                                                                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')}
