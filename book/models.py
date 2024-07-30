from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
        

class Author(models.Model):
    name = models.CharField(max_length=100)
    #books = models.ManyToManyField(Book)

    
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField(Author,related_name='books')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.title