from django.urls import path
from . import views
from .views import UpdatePostView

urlpatterns = [
    path('newsletter', views.newsletter, name='newsletter'),
    path("blog", views.blogs, name="blogs"),
    path("blog/<int:id>", views.blogs_comments, name="blogs_comments"),
    path("add_blogs", views.add_blogs, name="add_blogs"),
    path("edit_blog_post/<int:pk>",
         UpdatePostView.as_view(), name="edit_blog_post"),
    path("delete_blog_post/<int:id>",
         views.Delete_Blog_Post, name="delete_blog_post"),
    path("search", views.search, name="search"),
]
