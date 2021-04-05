from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    # указываем куда именно сохранять картинки для корректного отображения. "media/post_images"
    preview = models.FileField(upload_to='post_images', blank=True)
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {}'.format(self.pk, self.title)

    def get_absolute_url(self):
        return reverse("post_id_url", kwargs={"pk": self.pk})
    
    
# удаление медиафайлов при удалении поста
@receiver(pre_delete, sender=Post)
def preview_delete(sender, instance, **kwargs):
    if instance.preview.name:
        instance.preview.delete(False)
