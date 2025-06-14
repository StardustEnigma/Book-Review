from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator,MaxValueValidator

class Book(models.Model):
    Genre_Choices = [
    ('FIC', 'Fiction'),
    ('NF', 'Non-Fiction'),
    ('MYST', 'Mystery'),
    ('THRL', 'Thriller'),
    ('ROM', 'Romance'),
    ('SCI', 'Science Fiction'),
    ('FANT', 'Fantasy'),
    ('BIO', 'Biography'),
    ('HIST', 'Historical'),
    ('PHIL', 'Philosophy'),
    ('POET', 'Poetry'),
    ('HORR', 'Horror'),
    ('SELF', 'Self-help'),
    ('TECH', 'Technology'),
    ('BUS', 'Business'),
    ('SPIR', 'Spirituality'),
    ('EDU', 'Educational'),
    ('TRAV', 'Travel'),
    ('ART', 'Art & Photography'),
    ('COOK', 'Cooking'),
]
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    description=models.TextField()
    genre=models.CharField(max_length=20,choices=Genre_Choices)
    isbn=models.CharField('ISBN',max_length=13,unique=True)
    publication_date=models.DateField()
    avgRating=models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(0),MaxValueValidator(5)],
        default=0
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book_detail',kwargs={"pk": self.pk})
    