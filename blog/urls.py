from django.urls import path
from . import views


urlpatterns = [
    path('', views.Homepage.as_view(), name='hello_url'),
    path('portfolio/', views.Portfolio.as_view(), name='posts_url'),
    path('post/<int:pk>/', views.Posts_id.as_view(), name='post_id_url')
]
