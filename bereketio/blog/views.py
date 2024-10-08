from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from .models import Post, Comment


# posts = [
#     {
#         'author': 'Bereket',
#         'title': 'Your portfolio is stopping you from geting that job',
#         'content': 'An intense way to learn about the process and practice your designs skills — My 1st hackathon '
#                    'Hackathons have been on my mind since I heard it was a good way to gain experience as a junior UX '
#                    'designer. As my portfolio...',
#         'date_posted': '21.09.2024'
#     },
#     {
#         'author': 'Bob',
#         'title': 'Melody mobile app: a UI UX case study',
#         'content': 'An intense way to learn about the process and practice your designs skills — My 1st hackathon '
#                    'Hackathons have been on my mind since I heard it was a good way to gain experience as a junior UX '
#                    'designer. As my portfolio...',
#         'date_posted': '22.09.2024'
#     },
# ]


# Create your views here.d
# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ('-date_posted',)

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False