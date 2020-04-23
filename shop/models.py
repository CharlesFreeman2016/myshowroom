from django.db import models
from django.utils import timezone
from PIL import Image


class Product(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=9.99)
    image = models.ImageField(upload_to='products_pics', default='no-image.png')
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        img = Image.open(self.image.path)