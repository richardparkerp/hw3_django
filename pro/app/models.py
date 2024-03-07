from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Карта:"
        verbose_name_plural = "Карты"


