from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import BlogForm
from .models import Blog


def index(request):
    blogs = Blog.objects.all()
    return render(request, "blog/index.html", {"blogs": blogs})


def create(request):
    if request.method == "POST":
        form = BlogForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse("blog:index"))

    else:
        form = BlogForm()

    return render(request, "blog/create.html", {"form": form})


def update(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("blog:index"))
    else:
        form = BlogForm(instance=blog)

    context = {
        "blog": blog,
        "form": form,
    }

    return render(request, "blog/update.html", context)


def delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()

    return HttpResponseRedirect(reverse("blog:index"))
