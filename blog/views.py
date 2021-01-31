from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post, Category


class HomePost(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        return context


class GetPost(DetailView):
    model = Post
    template_name = 'blog/blog_post.html'
    context_object_name = 'post'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Blog'
    #     return context


class PostByCategory(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context
