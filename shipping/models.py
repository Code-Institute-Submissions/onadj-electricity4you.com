from django.db import models

class Country(models.Model):
    

    class Meta:
        verbose_name_plural = 'Countries'
        
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Deliverytime(models.Model):
    country = models.ForeignKey('Country', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()

    def __str__(self):
        return self.name