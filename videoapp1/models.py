from django.db import models

class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file = None

    def __str__(self):
        return self.name + ": " + str(self.videofile)


# Create your models here.
