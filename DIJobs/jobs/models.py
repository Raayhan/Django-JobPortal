from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return f'/{self.slug}/'

class Job(models.Model):
    
    category    = models.ForeignKey(Category,related_name='jobs', on_delete=models.CASCADE)
    title       = models.CharField(max_length=255)
    slug        = models.SlugField()
    description = models.TextField(blank=True,null=True)
    salary      = models.DecimalField(max_digits=8,decimal_places=2)
    date_added  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    
    def __str__(self):
        return self.title
    
    
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
