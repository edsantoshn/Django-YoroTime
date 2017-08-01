from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^authors/$', views.AuthorsIndex.as_view()),
    url(r'^posts/$', views.PostsIndex.as_view()),
    url(r'^posts/(?P<pk>\d+)/$', views.PostDetail.as_view()),
    url(r'^posts/author/(?P<fk>\d+)/$', views.AuthorPosts.as_view()),
    url(r'^posts/comment/(?P<fk>\d+)$', views.CommentsPost.as_view()),
    url(r'^posts/author/time/$', views.AuthorPostsSince.as_view()),
    url(r'^posts/author/time/$', views.AuthorPostsAfter.as_view()),
]
