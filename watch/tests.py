from django.test import TestCase
from .models import *

# Create your tests here.
class NeighbourhoodTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Juja = Business.objects.create(name="Juja")
        self.test_neighbourhood = NeighbourHood.objects.create(name='Membley',location='Nairobi',admin='Chacha',image='example.jpg',description='Beautiful place',occupants='1')
        self.test_neighbourhood.save()


    def test_save_method(self):
        self.test_neighbourhood.save()
        test_neighbourhoods = NeighbourHood.objects.all()
        self.assertTrue(len(test_neighbourhoods) > 0)
            
    
    def test_delete_method(self):
        self.Neighbourhood.delete_neighbourhood()
        neighbourhoods = NeighbourHood.objects.all()
        self.assertTrue(len(neighbourhoods)==0)   
        
    def tearDown(self):
        NeighbourHood.objects.all().delete()
        
        
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Prof= Profile( id = '1', user ='James',bio='Happy', profile_picture = 'example.jpg',email='chacha@gmail.com',phone_number='0724580020',neighbourhood='Membley' )
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Prof,Profile)) 
        
        
class PostTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Pos= Post( id = '1', user ='James',title='Happy', info = 'Happy day',neighbourhood='Membley' )
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Pos,Post))        
        

class AuthorityTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Auth= Post( id = '1', name ='Police',email='police@gmail.com', contact = '707594873',neighbourhood='Membley' )
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Auth,Authority))
        

class HealthTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Heal= Health( id = '1', name ='Hospital',email='hospital@gmail.com', contact = '707594873',neighbourhood='Membley' )
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Heal,Health))   
        
        
class BusinessTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Busi = Business.objects.create(name="Busi")

        self.test_business = Business.objects.create(name='Barber',image='example.jpg',user='Chacha',email='example@gmail.com',phone_number='072565676',neighbourhood='Membley')

        self.test_business.save()

    def test_save_method(self):
        self.test_business.save()
        test_business = Business.objects.all()
        self.assertTrue(len(test_business) > 0)
            
    
    def test_delete_method(self):
        self.Business.delete_business()
        business = Business.objects.all()
        self.assertTrue(len(business)==0)   
        
    def tearDown(self):
        Business.objects.all().delete()                                             