from django.db import models

# Create your models here.
class  Slider(models.Model):
    headline = models.CharField(max_length=255) 
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='media/slider')
    created_date = models.DateTimeField(auto_now_add = True)
    jump_to = models.URLField(max_length=255)

    def __str__(self):
        return self.headline    


class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255)
    insta_link = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="media/team/%Y/%m/%d/")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.first_name

