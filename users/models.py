from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
# The default user models provided by django doesnt have a field for profile picture, so we'll extend the user model and
# extend it to make it suit our needs.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='IMG_4243.JPG', upload_to='profile_pics')
    # add address and phone number    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        """ Overriding the save method so that we can resize images. Larger images
        are space inefficient and can also affect website efficiency."""
        super().save()

        img = Image.open(self.image.path)  # open the current image.
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)  # resize the image to 300 pixels
            img.save(self.image.path)



