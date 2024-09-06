from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class recipe_module (models.Model):
    user= models.ForeignKey(User, on_delete=models.SET_NULL ,null= True,blank=True)
    id= models.AutoField(primary_key=True)
    recipeName=models.CharField(max_length=100)
    recipeDescription=models.TextField()
    recipeImage=models.FileField(upload_to='documents/',default="")
    recipeImageUrl=models.TextField(default="")
  
