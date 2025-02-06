from django.db import models

# Create your models here.


class Job(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    job = models.ForeignKey(to=Job, on_delete=models.SET_NULL, null=True, default=None, blank=True)
    
    def __str__(self):
        return f'{self.name} - {self.job}'

class SubCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    category = models.CharField(max_length=50)
    subcat = models.ManyToManyField(SubCategory)


    def __str__(self):
        return f'{self.category} - {[str(i) for i in self.subcat.all()]}'

class ModelFood(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT, null=True, default='Anônimo', blank=True )
    slug = models.SlugField()
    subtitle = models.TextField(max_length=100)
    category_food = models.ForeignKey(Category, on_delete= models.SET_NULL, null=True, blank=True, default=None)
    
    price = models.DecimalField(decimal_places=2, max_digits=5)
    
    image = models.ImageField(upload_to='user/')
    description = models.TextField(max_length=150)
    
    date_create = models.DateTimeField(auto_now_add=True)
    data_atualization = models.DateTimeField(auto_now=True)

  
    def __str__(self):
        return f'{self.category_food}'
        
