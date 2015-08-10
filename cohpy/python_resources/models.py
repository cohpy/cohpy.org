from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'


class PythonResource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    link = models.TextField(blank=True)
    categories = models.ManyToManyField(Category)
    date_added = models.DateTimeField()
                
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


