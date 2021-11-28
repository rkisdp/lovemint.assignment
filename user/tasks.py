import os
from contextlib import suppress
from PIL import Image
from user.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from celery import shared_task


@receiver(post_save, sender=User)
def resize_image(sender, instance, created, **kwargs):
    if created:
        image_resize_handler.delay(instance.id)


@shared_task
def image_resize_handler(obj_id):
    user_entity = User.objects.get(id=obj_id)
    img = Image.open(os.path.join(settings.BASE_DIR) + user_entity.image.url)
    new_width, new_height = 320, 320
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    *new_path, img_name = str(user_entity.image.url).split('/')
    image_new_path = "/".join(new_path) + '/resize/'
    obj_new_path = os.path.join(settings.BASE_DIR) + "/" + image_new_path
    with suppress(FileExistsError):
        os.mkdir("/" + obj_new_path)
    img.save(obj_new_path + img_name)
    user_entity.resized_image = image_new_path.replace("media", "") + img_name
    user_entity.save()
    return True
