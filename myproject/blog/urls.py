# blog\urls.py
from django.urls import path
from .apps import BlogConfig
from .views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path("blog/", BlogListView.as_view(), name="post_list"),
    path("create/", BlogCreateView.as_view(), name="post_create"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("blog/edit/<int:pk>/", BlogUpdateView.as_view(), name="post_edit"),
    path("blog/delete/<int:pk>/", BlogDeleteView.as_view(), name="post_delete"),
]
