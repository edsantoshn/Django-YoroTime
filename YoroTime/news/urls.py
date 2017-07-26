from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^/$', views.AuthorsIndex.as_view()),
    url(r'^/$', views.PostsIndex.as_view()),
    url(r'^/$', views.PostDetail.as_view()),
    url(r'^/$', views.AuthorPosts.as_view()),
    url(r'^/$', views.CommentsPost.as_view()),
]
