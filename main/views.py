from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post, Comment
# from .forms import CommentForm
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ShowPostView(ListView):
    model = Post
    template_name = 'main/all-post.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 5

    def get_context_data(self, **kwards):
        ctx = super(ShowPostView, self).get_context_data(**kwards)

        ctx['title'] = 'Главная страница сайта'
        return ctx


class DetailPostView(DetailView):
    model = Post
    template_name = 'main/detail-post.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # определяем текущего пользователя
        auth_user = self.request.user
        context['auth_user'] = auth_user

        context['title'] = Post.objects.get(pk=self.kwargs['pk'])

        return context


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'main/create-post.html'

    fields = ['title', 'category', 'content']

    def get_context_data(self, **kwards):
        ctx = super(CreatePostView, self).get_context_data(**kwards)

        ctx['title'] = 'Добавление статьи'
        ctx['btn_text'] = 'Добавить статью'
        return ctx

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'main/create-post.html'

    fields = ['title', 'content']

    def get_context_data(self, **kwards):
        ctx = super(UpdatePostView, self).get_context_data(**kwards)

        ctx['title'] = 'Обновление статьи'
        ctx['btn_text'] = 'Обновить статью'
        return ctx

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.author:
            return True

        return False

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Descriptions """
    model = Post
    success_url = '/main/'
    template_name = 'main/delete-post.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True

        return False


class CreateCommentView(CreateView):
    """ класс для создания веб-сервиса по добавлению сокращаемых ссылок """
    model = Comment
    template_name = 'main/create-comment.html'

    fields = ['post', 'text']

    def get_context_data(self, **kwards):
        ctx = super(CreateCommentView, self).get_context_data(**kwards)

        ctx['title'] = 'Добавление комментария'
        ctx['btn_text'] = 'Добавить комментарий'
        return ctx

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        self.success_url = reverse_lazy('home')
        return super().form_valid(form)


