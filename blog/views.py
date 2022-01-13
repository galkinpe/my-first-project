from django.db.models.query import QuerySet
from django.views.generic import (
    ListView,
    TemplateView,
    FormView,
    UpdateView,
    DeleteView,
    DetailView,  
    CreateView,
)
from django.shortcuts import render
from django.utils import timezone
from .models import Record
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.views.generic import View


class PostList(ListView):
    model=Record
    template_name = 'blog/post_list.html'
    queryset = model.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    #def get(self, request):
       # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
       # return render(request, 'blog/post_list.html', {'posts': posts})


class PostDetail(DetailView):
    model=Record
    template_name = 'blog/post_detail.html'
    queryset = model.objects.all()

    #def get_queryset(self):
       # queryset = super().get_queryset()
       # return queryset.filter(author=self.request.user)

class PostNew(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
        return render(request, 'blog/post_edit.html', {'form': form})


class PostEdit(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
        return render(request, 'blog/post_edit.html', {'form': form})
