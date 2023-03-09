from django.urls import path
from . import views
app_name = 'item'
urlpatterns = [
    path('new-item/', views.newItem, name='new-item'),
    path('<int:pk>/', views.detail, name='detail'),
]