from django.db import models

class TVShow(models.Model):
    GENRE_CHOICE = (
        ('Detective', 'Detective'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Anime', 'Anime'),
        ('Romantic', 'Romantic')
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    quantity = models.IntegerField()
    genre = models.CharField(choices=GENRE_CHOICE, max_length=100)
    date_filmed = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class ShowComment(models.Model):
    shows = models.ForeignKey(TVShow, on_delete=models.CASCADE,
                              related_name="show_comment")
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.shows.title




