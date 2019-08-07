from django.shortcuts import render, get_object_or_404, reverse,redirect  # added these 3 for the link to the post shown in index
from .models import Post, Category
from django.db.models import Q
from .forms import CommentForm


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


def blog(request, id):
    category_list = Category.objects.all()
    most_recent = Post.objects.order_by('-timestamp')[:3]
    blog_list = Post.objects.all()
    post = get_object_or_404(Post, id=id)
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse('post-detail', kwargs={'id': post.id}))

    context = {
        'blog_list': blog_list,
        'post': post,
        'form': form,
        'most_recent': most_recent,
        'category_list': category_list,

    }
    return render(request, 'blog.html', context)


# def post(request, id):
#     return render(request, 'blog.html', {})