import threading

import cv2
from django.http import (HttpResponse, StreamingHttpResponse)
from django.views.decorators import gzip


@gzip.gzip_page
def video_stream_view_back(request):
    try:
        cam = VideoReader()
        return StreamingHttpResponse(cam.update(), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        return HttpResponse('Hi from back_video_stream_view')


class VideoReader(object):
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
            if self.grabbed:
                frame = self.get_frame()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
            else:
                yield None
