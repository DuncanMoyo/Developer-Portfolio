from django.shortcuts import render
from .models import Post
from django.db.models import Q


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')

    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()

        context = {
            'queryset': queryset
        }

        return render(request, 'search_results.html', context)


def blog(request):
    blog_list = Post.objects.all()
    context = {
        'blog_list': blog_list,
    }
    return render(request, 'blog.html', context)


def post(request, id):
    return render(request, 'post.html', {})