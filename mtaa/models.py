from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

  
class Hood(models.Model):
    # hood_photo = models.ImageField(upload_to='hoods/')
    hood_photo = CloudinaryField('hood_photo')
    hood_name = models.CharField(max_length=100, null=True)
    occupants_count = models.PositiveIntegerField(default=0)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    @classmethod
    def get_hoods(cls):
        hoods = Hood.objects.all()
        return hoods

    @classmethod
    def search_hood(cls,hood_search):
        hoods = cls.objects.filter(id__icontains = hood_search)
        return hoods

    class Meta:
        ordering = ['hood_name']


