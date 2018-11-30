from django.urls import path
from .views import PostListView , PostDetailView
from . import views
urlpatterns = [
    #path('',views.home,name='blog-home'),
    path('about/',views.about,name='blog-about'),
    path('',PostListView.as_view(),name='blog-home'),
    path('post/<pk>/',PostDetailView.as_view(),name='post-detail'),
]

