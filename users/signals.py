from django.db.models.signals import post_save  # signal for when an object gets saved.
from django.contrib.auth.models import User  # this will be sending the signal.
from django.dispatch import receiver  #Receives the signals and performs some tasks with it.
from .models import Profile


"""
With signals, we can ensure that a new profile is created every time a user makes an account.
When a user is saved, send this signal, which will be received by the receiver (create profile function)

"""
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """The post_save signals passes all these parameters. If the user is created, create
    a profile with the user as the instance of the user passed."""
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    """The post_save signals passes all these parameters. If the user is created, create
    a profile with the user as the instance of the user passed."""
    instance .profile.save()