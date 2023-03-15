from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Image


# function is only called if the m2m_changed signal has been launched by this sender.
@receiver(m2m_changed, sender=Image.users_like.through)
def users_like_changed(sender, instance, **kwargs):
    instance.total_likes = instance.users_like.count()
    instance.save()
