from django.contrib import admin
from django.urls import path, include
from api import views
urlpatterns = [
    path('contacts/<int:contact_id>', views.ContactsView.as_view(), name='id-contacts'),
    path('contacts/', views.ContactsView.as_view(), name='all-contacts'),
    path('games/', views.GamesViews.as_view(), name='all_games'),
    path('todo/', views.TodosView.as_view(), name='all-todos'),
    path('todo/<int:todo_id>', views.TodosView.as_view(), name='all_todos'),
]
