from django.urls import path
from . import views

app_name = "parse"
urlpatterns = [
    # path("parser/", views.ParserFormView.as_view(), name="parse_func"),
    path('films/', views.FilmView.as_view(), name='film'),
    path('parser/', views.ParserFilmView.as_view(), name='parser')

    # path('films/', views.FilmView.as_view(), name='film'),
    # path('parser/', views.ParserFilmView.as_view(), name='parser')
]
