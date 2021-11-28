from django.db import models
from django.contrib.gis.db import models as geo_field
import uuid
# Create your models here.


def file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = 'user/upload/{}.{}'.format(uuid.uuid4().hex, ext)
    return filename


def resize_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = 'user/upload/resize/{}.{}'.format(uuid.uuid4().hex, ext)
    return filename


class User(models.Model):
    name = models.CharField(
        max_length=64
    )
    age = models.PositiveSmallIntegerField(
        default=0
    )
    image = models.ImageField(
        upload_to=file_path,
        null=True,
        blank=True
    )
    resized_image = models.ImageField(
        upload_to=resize_file_path,
        null=True,
        blank=True
    )
    gender = models.CharField(
        choices=(
            ('Male', 'MALE'),
            ('Female', 'FEMALE'),
        ),
        max_length=8
    )
    description_text = models.CharField(
        max_length=128,
        null=True,
        blank=True
    )
    location = geo_field.PointField(
        max_length=512,
        null=True,
        blank=True
    )
    timestamp = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('-id',)

    def __unicode__(self):
        return f'{self.id} - {self.name}'

    def __str__(self):
        return f'{self.id} - {self.name}'
