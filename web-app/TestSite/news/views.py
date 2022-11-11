from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin

from . import pars
from .models import Articles, LikesDislikes, Categories, Comment
from .forms import ArticleForm, CommentForm, DeleteCommentForm
from django.views.generic import DetailView, UpdateView, DeleteView

from register.models import Profile
from django.db.models import Q
import requests
from bs4 import BeautifulSoup as bs




def news_home(request):
    news = Articles.objects.order_by('-date')
    categories = Categories.objects.all()

    return render(request, 'news/news_home.html', {'news': news, 'categories': categories,})

def news_liked(request):
    a = LikesDislikes.objects.filter(user_like=request.user.id)
    b = []
    for i in a:
        if i.like_or_dislike == 'like':
            b.append(i.state_like)
    categories = Categories.objects.all()
    return render(request, 'news/news_liked.html', {'news_liked': b, 'categories': categories})


class NewsDetailView(FormMixin, DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'
    form_class = CommentForm
    success_msg = 'Комментарий успешно создан!'



    def get_success_url(self, **kwargs):
        return reverse_lazy('news-detail', kwargs={'pk': self.get_object().id})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.article = self.get_object()
        self.object.commentator = self.request.user
        self.object.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)




    def get_context_data(self, **kwargs):
        categories = Categories.objects.all()
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.all()
        context['comment_delete'] = DeleteCommentForm
        context['categories'] = categories
        return context




class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticleForm

    def get_context_data(self, **kwargs):
        categories = Categories.objects.all()
        context = super(NewsUpdateView, self).get_context_data(**kwargs)
        context['categories'] = categories
        return context

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'

    def get_context_data(self, **kwargs):
        categories = Categories.objects.all()
        context = super(NewsDeleteView, self).get_context_data(**kwargs)
        context['categories'] = categories
        return context


def create(request):
    #pars.CreateState()  #Парсер статей
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            AuthArt = form.save(commit=False)
            AuthArt.creater_id = request.user.id
            AuthArt.creater_username = request.user.username
            AuthArt.author = request.user
            AuthArt.save()
            return redirect('news_home')
    else:
        form = ArticleForm()
    categories = Categories.objects.all()
    date = {
        'form': form,
        'error': 'Форма была неверной',
        'categories': categories
    }

    return render(request, 'news/create.html', date)

def create_state():
    pars_article = Articles(title='')

def like_news(request):
    user = request.user
    if request.method == 'POST':
        news_id = request.POST.get('news_id')
        news_obj = Articles.objects.get(id=news_id)

        if user in news_obj.liked.all():
            news_obj.liked.remove(user)
        else:
            news_obj.liked.add(user)

        like, created = LikesDislikes.objects.get_or_create(user_like=user, state_like=news_obj)

        if not created:
            if like.like_or_dislike == 'like':
                like.like_or_dislike = 'dislike'
            else:
                like.like_or_dislike = 'like'
        else:
            like.like_or_dislike = 'like'
        like.save()
        return redirect(f'/news/{news_id}')

    return redirect(f'/news')




def search(request):
    search_query = request.GET.get('search', '')
    if search_query:
        news = Articles.objects.filter(Q(title__icontains=search_query) | Q(full_text__icontains=search_query))
    else:
        news = Articles.objects.all()
    categories = Categories.objects.all()
    date = {
        'news': news,
        'categories': categories,
    }
    return render(request, 'news/search.html', date)



def cat(request, category):
    c = Categories.objects.filter(categories_title=category)
    categories = Categories.objects.all()
    if c:
        for i in c:
            states = Articles.objects.filter(categories_id=i.id)
    else:
        states = None
    date = {
        'categories': categories,
        'states': states,
    }
    return render(request, f'news/{category}.html', date)



