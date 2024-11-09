from django.urls import path
from .import views
urlpatterns=[
# Urls for users api
path('users/',views.get_users,name='get_users'),
path('users/create',views.create_user,name='create_users'),
path('users/<int:pk>',views.user_detail,name='user_detail'),
# Urls for Authors  api
path('authors/',views.get_authors,name='get_author'),
path('authors/create',views.create_author,name='create_author'),
path('authors/<int:pk>',views.author_detail,name='author_detail'),

# Urls for Articles api
path('articles/',views.get_articles,name='get_article'),
path('articles/create/<int:author_id>',views.create_article,name='create_article'),
path('articles/<int:pk>',views.single_article,name='single_article'),

# Urls for Comments api
path('comments/',views.get_comments,name='get_comments'),
path('comments/create/<int:pk>',views.create_comment,name='create_comment'),
path('comments/<int:pk>',views.single_comment,name='single_comment'),


]
