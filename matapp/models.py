from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Matzip(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='image/')
    image2 = models.ImageField(upload_to='image2/', null=True)
    image_thumnail = ImageSpecField(source='image', processors=[ResizeToFill(150, 100)])

    def __str__(self):
        return self.title
    def sum(self):
        return self.body[:50]


