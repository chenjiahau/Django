from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.ItemView.as_view(), name='item'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('edit/<int:item_id>/', views.edit, name='edit'),
]
