from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from . models import Post


class Homepage(View):
    def get(self, request):
        return render(request, 'blog/main.html')


class PostList(ListView):
    model = Post # или queryset = Post.object.all()
    context_object_name = 'posts'
    template_name = 'blog/portfolio.html'
# class Portfolio(View):
#     def get(self, request):
#         posts = Post.objects.all()
#         return render(request, 'blog/portfolio.html', context={'posts': posts})


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_page.html'
# class Posts_id(View):
#     def get(self, request, pk):
#         id = Post.objects.get(pk=pk)
#         # элемент в цикле
#         return render(request, 'blog/post_page.html', context={'post': id})
