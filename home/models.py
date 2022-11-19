from django.db import models
from PIL import Image

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    freelance = models.CharField(max_length=100)
    projects = models.CharField(max_length=100)
    year_of_experience = models.CharField(max_length=100)
    pic = models.ImageField(upload_to="about_pics/", default='default.png')


    def __str__(self):
        return self.name

class expertie(models.Model):

    tech = models.CharField(max_length=100)
    skill_level = models.CharField(max_length=100)

    
    def __str__(self):
        return self.tech
    
class Resume(models.Model):
    article = models.TextField()
    education_level = models.CharField(max_length=100)
    ed_year = models.CharField(max_length=100)
    ed_place = models.CharField(max_length=100)
    educ_experience_description = models.CharField(max_length=100)

    def __str__(self):
        return self.education_level
    
class professional_experience(models.Model):
    on =  models.CharField(max_length=100)
    period = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.on
    
class service(models.Model):
    service_type = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.service_type

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        img= Image.open(self.picture.path)
        if img.height >300 or img.width >300:
            output_size = (150,150)
            img.thumbnail(output_size)
            img.save(self.picture.path)


class projects(models.Model):
    title = models.CharField(max_length=100)
    nameof_pr= models.CharField(max_length=200)
    pic = models.ImageField(upload_to='projects/')

    

    def __str__(self):
        return self.title

class price(models.Model):

    service_type = models.CharField(max_length=200)
    price_money = models.CharField(max_length=50)

 

    def __str__(self):
        return self.service_type
class contact_me(models.Model):
    facebook = models.CharField(max_length=150)
    insta = models.CharField(max_length=150)
    telegram = models.CharField(max_length=150)
    linkedin = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone_no = models.CharField(max_length=150)

    def __str__(self):
        return "Contact information"
    