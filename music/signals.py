from .models import Album
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Album)
def index_post(sender, instance, **kwargs):
    instance.indexing()
