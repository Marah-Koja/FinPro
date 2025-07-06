from django.db import models
from django.contrib.auth.models import User


class Applications(models.Model):
    name = models.CharField(max_length=100)
    package_id = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image_path = models.CharField(max_length=255)  # مسار الصورة في مجلد static
    rating = models.FloatField(default=0.0)

    def str(self):
        return self.name
   
 



