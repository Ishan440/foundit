from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from django.urls import reverse
from PIL import Image

# Create your models here.


class Listing(models.Model):
    Title = models.CharField(max_length =100)
    Description = models.TextField()
    Date = models.DateTimeField(default=timezone.now)
    Image = models.ImageField(default='sample', upload_to='lost_pics')
    Place = models.CharField(max_length =100)
    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self):
        """ Overriding the save method so that we can resize images. Larger images
        are space inefficient and can also affect website efficiency."""
        super().save()

        img = Image.open(self.image.path)  # open the current image.
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)  # resize the image to 300 pixels
            img.save(self.image.path)