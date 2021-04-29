from django.urls import path     
from . import views


urlpatterns = [
    path('', views.book),
    path('add_book',views.add_book),
    path('add_author',views.add_author),
    path('authors', views.author),
    path('view_book/<id>', views.view_book),
    path('view_author/<id>',views.view_author)
    
]