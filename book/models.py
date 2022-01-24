from django.db import models

class Genre(models.Model):
    GENRE_CHOICE = (
        ('Detective', 'Detective'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Romantic', 'Romantic'),
        ('Anime', 'Anime')
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    quantity = models.IntegerField()
    genre = models.CharField(choices=GENRE_CHOICE, max_length=100, null=True)
    date_publication = models.DateField()

    def __str__(self):
        return self.title

class BookComment(models.Model):
    book = models.ForeignKey(Genre, on_delete=models.CASCADE,
                             related_name="book_comment")
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.book.title

class Expert(models.Model):
    name = models.CharField(max_length=20, null=True)
    surname = models.TextField()
    date_of_birth = models.TextField()
    activity = models.TextField()


    def __str__(self):
        return self.name

class ExpertRecomendation(models.Model):
    expert = models.ForeignKey(Genre, on_delete=models.CASCADE,
                               related_name="expert_info", null=True)
    recomendation_text = models.TextField(null=True)
    courses = models.ManyToManyField(Expert, related_name="info_exp")


    def __str__(self):
        return self.expert
































