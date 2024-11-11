from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipie(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null= True,blank=True)
    receipe_name = models.CharField(max_length=100)
    receipe_desc = models.TextField()
    receipe_img = models.ImageField(upload_to="receipe")

    def __str__(self) -> str:
        return self.receipe_name
