from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_list, name='post_lists_url'),
    path('post/<slug>/', PostDetail.as_view(), name='post_details_url'),
    path('posts/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('post/<slug>/delete', PostDelete.as_view(), name='post_delete_url'),
    path('tags/', tags_list, name='tag_lists_url'),
    path('tags/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<slug>/', TagDetail.as_view(), name='tag_details_url'),
    path('tag/<slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<slug>/delete', TagDelete.as_view(), name='tag_delete_url')
]
