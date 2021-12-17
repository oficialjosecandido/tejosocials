from django.db import models
from taggit.managers import TaggableManager
import datetime

# Create your models here.


class Post(models.Model):
    tag = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=200)
    #slug = models.SlugField(unique=True, max_length=100)
    #tags = TaggableManager()
    date = models.DateTimeField(auto_now_add=True)
    excerpt = models.CharField(max_length=150, blank=True, null=True)
    sku = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.title} from {self.author} - {self.date}"


class Contact(models.Model):
    contactId = models.AutoField(primary_key=True)
    time = models.DateField(auto_now_add=True)
    senderName = models.CharField(max_length=100, blank=True, null=True)
    senderEmail = models.CharField(max_length=100, blank=True, null=True)
    senderMessage = models.TextField(blank=True, null=True)
    senderSKU = models.CharField(max_length=100, blank=True, null=True)
    stata = (
        ('Completed', 'Completed'),
        ('Pending', 'Pending'),
        ('Unread', 'Unread')
    )
    status = models.CharField(max_length=64, choices=stata)

    def __str__(self):
        return f"Received a message from {self.senderEmail} on {self.time} and the  status is {self.status}"
