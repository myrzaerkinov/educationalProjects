from django.urls import path
from . import views

app_name = 'shows'
urlpatterns = [
    path('shows/', views.shows_all, name='shows_all'),
    path('shows/<int:id>/', views.shows_detail, name='shows_detail'),
    path('shows/<int:id>/update/', views.show_update, name='show_update'),
    path('shows/<int:id>/delete/', views.show_delete, name='show_delete'),
    path('add-shows/', views.add_show, name='add-shows'),
]
