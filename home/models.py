from django.db import models

# Create your models here.
class Banner(models.Model):
    content = models.CharField(max_length=250)


    def __str__(self):
        
        return self.content

class SpanishBanner(models.Model):
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.text
class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10, blank=True)
    comment = models.CharField(max_length=500)
    worked = models.BooleanField(default=False)

    def __str__(self):
        return self.name
