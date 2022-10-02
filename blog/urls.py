from django.urls import path
<<<<<<< HEAD
from .views import BlogListView, BlogDetailView
=======
from .views import AboutPageView, BlogListView, BlogDetailView

>>>>>>> ckeditor

urlpatterns = [
    path('post/<slug:slug>/', BlogDetailView.as_view(), 
        name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]