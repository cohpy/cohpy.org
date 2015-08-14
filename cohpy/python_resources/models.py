from django.db import models

import pdb
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


    def comma_separated_categories(self):
        category_list = []
        categories = Category.objects.filter(pythonresource__pk=self.id)
        # pdb.set_trace()
        for category in categories:
            category_list.append(category.name)
        return ', '.join(category_list)



