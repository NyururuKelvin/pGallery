from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.

# Image Model Tests
class TestImage(TestCase):
    # testing Image Model
    def setUp(self):
        self.location1=Location(location='Home')
        self.location1.save_location()
        self.category1=Category(category='Hobby')
        self.category1.save_category()
        self.image1=Image(name='Testing',description='Test image',location=self.location1,category=self.category1)
        self.image1.save_image()

    # Obects saved test   
    def test_save_image(self):
        self.category1.save_category()
        self.location1.save_location()
        self.image1.save_image()
        
    # Objects updated
    def test_updated_image(self):
        update=Image.update_image(self.image1.name,'Updated Test')
        self.assertEqual(update.name,'Updated Test')
     
    # Delete image test  
    def test_delete_image(self):
        Image.delete_image(self.image1.name)
        self.assertTrue(len(Image.objects.all())==0)
        
    # Get image by Id test
    def test_get_image_by_id(self):
        image=Image.get_image_by_id(self.image1.pk)
        self.assertEqual(image.name,self.image1.name)
        
    # Searsch Image by Category test
    def test_search_category(self):
        image=Image.search_category(self.image1.name.name)
        self.assertTrue(len(image)>0)
    
    # Filter by Location test
    def test_filter_by_location(self):
        image=Image.filter_by_location(self.image1.location.location)
        self.assertTrue(len(image)>0)
        
    
# Location Model Tests       
class TestLocation(TestCase):
    # testing Location Model
    def setUp(self):
        self.location=Location(location='home')
        self.location.save_location()
    
    def tearDown(self):
        Location.objects.all().delete()
            
    def test_location_save(self):
        self.location.save_location()
        
    def test_update_location(self):
        update=Location.update_location(self.location.location,'School')
        self.assertEqual(update.location,'School')
        
    def test_delete_location(self):
        delete=Location.delete_location(self.location)
        self.assertTrue(len(Location.objects.all())==0)
        
        
        
        
# Category Model Tests
class TestCategory(TestCase):
    # testing Category Model
    def setUp(self):
        self.category=Category(category='Hobby')
        self.category.save()
        
        
    def test_category_saved(self):
        self.category.save_category()
        
    def test_update_category(self):
        update=Category.update_category(self.category.category,'Work')
        self.assertEqual(update.category,'Work')
        
    def test_delete_category(self):
        Category.delete_category(self.category.category)
        self.assertTrue(len(Category.objects.all())==0)