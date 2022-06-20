from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
from django.db.models import Q

# Create your models here.
class NeighbourHood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    admin = models.ForeignKey(User,on_delete = models.CASCADE,related_name='administration',null=True)
    image = CloudinaryField('image')
    description = models.CharField(max_length=250)
    occupants = models.IntegerField(default=0, null=True, blank=True)
    posted_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name 
    
    def create_neighborhood(self):
        """
        A method that creates a neighbourhood
        """
        self.save()
        
    def delete_neighborhood(self):
        """
        A method that deletes a neighbourhood
        """
        self.delete()    
        
    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        """
        A method that finds a neighbourhood using its id
        """
        return cls.objects.filter(id=neighborhood_id) 
    
    @classmethod
    def update_neighbourhood(cls, id):
        """
        A method that updates a neighbourhood
        """
        neighbourhood = cls.objects.filter(id=id).update(id=id)
        return neighbourhood       


# Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = CloudinaryField('image')
    bio = models.CharField(max_length=250)
    email =  models.CharField(max_length=60)
    phone_number = models.IntegerField(blank=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.SET_NULL, null=True, related_name='neighbour', blank=True)
    posted_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.user    
  
  
# Business Model    
class Business(models.Model):
    name = models.CharField(max_length=200)
    image = CloudinaryField('image')
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)     
    email =  models.CharField(max_length=60)
    phone_number = models.IntegerField(blank=True)
    neighbourhood = models.ForeignKey(NeighbourHood,on_delete=models.CASCADE, related_name='business',null=True)
    posted_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return self.name      
    
    def create_business(self):
        """
        A method that creates a business
        """
        self.save()

    def delete_business(self):
        """
        A method that deletes a business
        """        
        self.delete()
            
    @classmethod
    def search_business(cls,search_term):
        """
        A method that searches a business
        """          
        businesses = cls.objects.filter(name__icontains = search_term).all()
        return businesses 
    
    @classmethod
    def find_business(cls, business_id):
        """
        A method that finds a business using its id
        """         
        business = Business.objects.filter(id=business_id)
        return business  
    
    @classmethod
    def update_business(cls, id):
        """
        A method that updates a business using its id
        """  
        business = cls.objects.filter(id=id).update(id=id)
        return business
    

# Post Model
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    info =  HTMLField()
    neighbourhood= models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='neighbourhood_post')
    posted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
         
    @classmethod
    def get_post(cls, id):
        """
        A method that gets a post using the given id
        """   
        post = Post.objects.filter(id=neighbourhood_id)
        return post     
    
    
    
# Authority Model 
class Authority(models.Model):
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    neighbourhood = models.ForeignKey(NeighbourHood,on_delete=models.CASCADE)
 
    def __str__(self):
        return self.name      
    
    
# Health Model   
class Health(models.Model):
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    neighbourhood = models.ForeignKey(NeighbourHood,on_delete=models.CASCADE)
 
    def __str__(self):
        return self.name  