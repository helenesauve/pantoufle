from django.urls import path
from .views import AboutPageView, BlogListView, BlogDetailView


urlpatterns = [
    path('post/<slug:slug>/', BlogDetailView.as_view(), 
        name='post_detail'),
    path('', BlogListView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]