# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model): 
    """
    Django model Post(saved in the database)
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #link to another model
    title = models.CharField(max_length=200) #text with limited number of characters
    text = RichTextUploadingField(blank=True, null=True)
    # text = models.TextField() #text without limit
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now) 
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title