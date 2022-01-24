from django.urls import path
from . import views

app_name = 'shows'
urlpatterns = [
    path('shows/', views.ShowsListView.as_view(), name='shows_all'),
    path('shows/<int:id>/', views.ShowsDetailView.as_view(), name='shows_detail'),
    path('shows/<int:id>/update/', views.ShowsUpdateView.as_view(), name='show_update'),
    path('shows/<int:id>/delete/', views.ShowsDeleteView.as_view(), name='show_delete'),
    path('add-show/', views.ShowsCreateView.as_view(), name='add-shows'),
]
