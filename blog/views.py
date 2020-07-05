from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.http import HttpResponse
from .models import Post, Tag
from .utils import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_details.html'

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_details.html'

class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    Form = TagForm
    template = 'blog/tag_create.html'

class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
        Form = PostForm
        template = 'blog/post_create.html'

class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    template = 'blog/tag_update.html'
    Form = TagForm

class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    template = 'blog/post_update.html'
    Form = PostForm
    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     form = TagForm(instance=tag)
    #     return render(request, 'blog/tag_update.html', context={'form': form, 'tag': tag})
    #
    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     form = TagForm(request.POST, instance=tag)
    #     if form.is_valid():
    #         new_tag = form.save()
    #         return redirect(new_tag)
    #     return render(request, 'blog/tag_update.html', context={'form': form, 'tag': tag})

class PostDelete(LoginRequiredMixin, ObjectDeleteMixin,View):
    model = Post
    template = 'blog/post_delete.html'
    raise_exception = True
class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete.html'
    raise_exception = True
