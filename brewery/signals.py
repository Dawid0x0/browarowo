from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Place

@receiver(pre_save, sender=Place)
def my_handler(sender, instance, *args, **kwargs):
    if not instance.slug:
		instance.slug = slugify(instance.name)