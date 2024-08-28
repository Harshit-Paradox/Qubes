from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False,null=False)
    message = models.TextField(blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Affilate(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Builder(models.Model):
    USER_TYPE_CHOICES = [
        ('buyer', 'Are you a buyer?'),
        ('broker', 'Are you a broker?'),
    ]
    
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES , blank=False)  # Removed default
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    


class Career(models.Model):
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, blank=False)
    number = models.CharField(max_length=15, blank=False)
    city = models.CharField(max_length=100, blank=False)
    position = models.CharField(max_length=100, default="Site Head", editable=False)
    resume = models.FileField(upload_to='resumes/', blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.position}"



class Details(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    contact_number = models.CharField(max_length=20, blank=False, null=False)
    rera_number = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


