from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Speech(models.Model):
    Speaker = models.CharField(max_length = 30)
    title = models.CharField(max_length = 80)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Speaker(models.Model):
    firstname = models.CharField(max_length = 40)
    lastname = models.CharField(max_length = 40)
    info = models.TextField('Speech')
    
    def get_absoulte_url(self):
        return reverse('speaker_detail', args = [str(self.id)])
    
    def __str__(self):
        return self.firstname
    
    def __str__(self):
        return self.lastname
   
    
    
    
    
    
    
