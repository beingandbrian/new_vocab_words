from django.db import models
from django.utils import timezone

# Create your models here.
class VocabWord(models.Model):
    word = models.CharField(max_length=50, null=False)
    definition = models.CharField(max_length=500, null=False)
    sentence = models.CharField(max_length=500, null=False)
    publish_date = models.DateTimeField()
    creator = models.ForeignKey('Creator', on_delete=models.SET_NULL, null=True, related_name='vocab_word')

    def __str__(self):
        return f'{self.word} | {self.creator.last_name}, {self.creator.first_name}'
    
class Creator(models.Model):
    first_name = models.CharField(max_length=100, null=False, default="Brian")
    last_name = models.CharField(max_length=100,null=False, default="Lyew")
    full_name = models.CharField(max_length=100, null=False, default="Brian Lyew")
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
        