from django.urls import path
from .views import post_model_list_view, post_model_detail_view , post_model_create_view, post_model_update_view, post_model_delete_view

app_name = 'blog'


urlpatterns = [
    path("", post_model_list_view, name='blog_list'),
    path("<int:id>", post_model_detail_view, name='blog_detail'),
    path("create", post_model_create_view, name='blog_create'),
    path("<int:id>/edit", post_model_update_view, name='blog_edit'),
    path("<int:id>/delete", post_model_delete_view, name='blog_delete'),

    
]