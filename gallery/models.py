from django.db import models

# Models.
class Image(models.Model):
    image= models.ImageField(upload_to = 'articles/', default='No Image')
    image_description=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    location=models.ForeignKey('Location',on_delete=models.CASCADE)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)

    # Methods

    # Saving the image
    def save_image(self):
        self.save()

class Location(models.Model):
    location=models.CharField(max_length=30)

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

    def __str__(self):
        return self.category