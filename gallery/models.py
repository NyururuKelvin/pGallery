from django.db import models

# Models.
class Image(models.Model):
    image= models.ImageField(upload_to = 'articles/', default='No Image')
    title= models.CharField(max_length =60)
    image_description=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    location=models.ForeignKey('Location',on_delete=models.CASCADE)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)

    # Methods

    # Saving the image
    def save_image(self):
        self.save()
    
    # Updating the image
    @classmethod
    def update_image(cls,name,update):
        Image.objects.filter(image_name=name).update(image_name=update)
        update=Image.objects.get(image_name=update)
        return update    
        
    # Deleting the image    
    @classmethod    
    def delete_image(cls,image):
        Image.objects.get(image_name=image).delete()
        
    # Getting image by ID
    @classmethod
    def get_image_by_id(cls,id):
        image=Image.objects.get(pk=id)
        return image
    
    # Searching images
    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images

    # Filtering images by location 
    @classmethod
    def filter_by_location(cls,image_location):
        locations=Location.objects.filter(location=image_location)
        for location in locations:
            images=Image.objects.filter(location=location)
        return images
    
    def __str__(self):
        return self.image_name

class Location(models.Model):
    location=models.CharField(max_length=30)

    def __str__(self):
        return self.location

    # Updating the location
    @classmethod
    def update_location(cls,name,update):
        Location.objects.filter(location=name).update(location=update)  
        updated=Location.objects.get(location=update)
        return updated

        
    # Deleting the location   
    @classmethod    
    def delete_location(cls,location):
        deleted=Location.objects.get(location=location).delete()
        return deleted
    
    def __str__(self):
        return self.location

CATEGORY=[
        ('Educational','Educational'),
        ('Hobby','Hobby'),
        ('Family','Family'),
        ('Fashion','Fashion'),
        ('Sports','Sports'),
]
class Category(models.Model):
    category=models.CharField(max_length=15,choices=CATEGORY)
    
    # Methods

    # Saving the category
    def save_category(self):
        self.save()

    # Updating the Category
    @classmethod
    def update_category(cls,name,update):
        Category.objects.filter(category=name).update(category=update)
        update=Category.objects.get(category=update)
        return update    
        
    # Deleting the image   
    @classmethod    
    def delete_category(cls,category):
        Category.objects.get(category=category).delete()

    def __str__(self):
        return self.category