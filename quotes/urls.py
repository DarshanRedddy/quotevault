from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_quote, name='add_quote'),
    path('edit/<int:quote_id>/', views.edit_quote, name='edit_quote'),
    path('delete/<int:quote_id>/', views.delete_quote, name='delete_quote'),
    path('tag/<int:tag_id>/', views.quotes_by_tag, name='quotes_by_tag'),
]