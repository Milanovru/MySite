from django.db import models
from django.utils import timezone
from django.shortcuts import reverse


# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    # указываем куда именно сохранять картинки для корректного отображения. "media/post_images"
    preview = models.FileField(upload_to='post_images', blank=True)
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.id, self.title)

    def get_absolute_url(self):
        return reverse("post_id_url", kwargs={"id": self.id})
    