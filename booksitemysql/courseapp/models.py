from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import BaseUserManager


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_editor = models.BooleanField(default=False)


class FavoriteBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    class Meta:
        unique_together = [['user', 'book']]

class Category(models.Model):
    name = models.CharField('Categories', max_length=50)
    slug = models.SlugField(max_length=50)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    cover_image = models.ImageField(upload_to='img', blank=True, null=True)
    author = models.CharField(max_length=50)
    summary = models.TextField()
    author_summary = models.TextField()
    category = models.ManyToManyField(Category, related_name='books')
    recommended_books = models.BooleanField(default=False)
    ukrainian_books = models.BooleanField(default=False)
    bestsellers_books = models.BooleanField(default=False)
    average_rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title

    def update_average_rating(self):
        ratings = Rating.objects.filter(book=self)
        if ratings.exists():
            average = ratings.aggregate(Avg('rating'))['rating__avg']
            self.average_rating = round(average, 1)
        else:
            self.average_rating = None
        self.save()

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = [['user', 'book']]

@receiver(post_save, sender=Rating)
def update_book_average_rating(sender, instance, **kwargs):
    book = instance.book
    book.update_average_rating()

class BookSearch(models.Model):
    name_of_book = models.CharField(max_length=100)
    def __str__(self):
        return self.name_of_book


class UserManager(BaseUserManager):
    pass