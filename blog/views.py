from django.shortcuts import render
from django.views import View
from . models import Post


# Create your views here.
class Homepage(View):
    def get(self, request):
        return render(request, 'blog/main.html')


class Portfolio(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/portfolio.html', context={'posts': posts})


class Posts_id(View):
    def get(self, request, id):
        id = Post.objects.get(id=id)
        return render(request, 'blog/post_page.html', context={'post': id}) # элемент в цикле


