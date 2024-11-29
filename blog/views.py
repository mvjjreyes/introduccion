from django.shortcuts import render, get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView, DeleteView
from .forms import PostCreateForm
from .models import Post
from datetime import datetime
import locale
from django import forms

# Create your views here.
class BlogListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        ruta_imagen = 'images/logo.svg'
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        fecha_actual = datetime.now()
        fecha_formato = fecha_actual.strftime('%A, %d de %B de %Y')
        context = {
            'posts': posts,
            'ruta_imagen': ruta_imagen,
            'fecha_actual': fecha_formato,
        }
        return render(request, 'blog_list.html', context)


class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        fecha_actual = datetime.now()
        fecha_formato = fecha_actual.strftime('%A, %d de %B de %Y')
        context = {
            'form': form,
            'fecha_actual': fecha_formato,
        }
        return render(request, 'blog_create.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = PostCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')

                p, created = Post.objects.get_or_create(title=title, content=content)
                p.save()
                return redirect('blog:home')

        context = {}
        return render(request, 'blog_create.html', context)

class BlogDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        context = {
            'post': post,
        }
        return render(request, 'blog_detail.html', context)

class BlogUpdateView(UpdateView):
    model=Post
    fields=['title', 'content']
    template_name='blog_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('blog:detail', kwargs={'pk': pk})

class BlogDeleteView(DeleteView):
    model=Post
    template_name='blog_delete.html'
    success_url=reverse_lazy('blog:home')