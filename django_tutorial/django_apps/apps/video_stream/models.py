from django.db import models

# Create your models here.

# def user_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return 'user_{0}/{1}'.format(instance.user.id, filename)


class Video(models.Model):
    title = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    video_file = models.FileField(upload_to=f'media/%Y_%m_%d')

    def __str__(self):
        return self.title + '_' + str(self.creation_date.isoformat(" ", "seconds"))
