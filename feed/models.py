from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Article(models.Model):
    title = models.CharField(max_length=140, blank=False)
    content = models.TextField(blank=True)
    slug = models.CharField(max_length=140, unique=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title