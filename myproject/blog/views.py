# blog/views.py
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from blog.models import Record

class BlogListView(ListView):
    model = Record
    template_name = "blog/post_list.html"
    context_object_name = "blogs"

    def get_queryset(self):
        return Record.objects.filter(is_published=True)


class BlogCreateView(CreateView):
    model = Record
    fields = ["title", "content", "preview_image", "published", "views_count"]
    template_name = "blog/post_create.html"
    success_url = reverse_lazy("blog:post_list")


class BlogDetailView(DetailView):
    model = Record
    template_name = "blog/post_detail.html"
    context_object_name = "blog"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_number += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Record
    fields = ["title", "content", "preview_image", "published"]
    template_name = "blog/post_edit.html"
    success_url = reverse_lazy("post_list")

    def get_success_url(self):
        return reverse("blog:post_detail", args=[self.object.id])


class BlogDeleteView(DeleteView):
    model = Record
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("blog:post_list")
