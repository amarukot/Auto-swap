from django.db import models

class Seller(models.Model):
    name = models.CharField(default='', max_length=200)
    phone = models.CharField(default='', max_length=50)
    address = models.CharField(default='', max_length=400)
    web_site = models.URLField(default='', max_length=500)
    logo = models.URLField(default='', max_length=500)
    
    def __str__(self):
      return self.name

class Car(models.Model):
  make = models.CharField(default='', max_length=200)
  model = models.CharField(default = '', max_length= 500)
  trim = models.CharField(default = '', max_length= 500)
  img_url = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg',max_length= 500, unique=True)
  milage = models.CharField(default = '', max_length= 500)
  color = models.CharField(default = '', max_length= 500)
  name = models.ForeignKey(Seller, on_delete = models.CASCADE, related_name = 'car')
  
  def __str__(self):
    return self.model
 
