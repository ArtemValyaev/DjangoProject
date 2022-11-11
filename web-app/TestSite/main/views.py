from django.shortcuts import render
from django.http import HttpResponse
from news.models import Articles, LikesDislikes, Categories

from register.models import Profile


def recomendations(request):
    user_like = LikesDislikes.objects.filter(user_like_id=request.user.id, like_or_dislike='like') #QuerySet из нужных
    a = []
    for i in user_like:
        a.append(Articles.objects.filter(id=i.state_like_id)) #Список - QuerySet - Список
    b = []
    for i in a:
        for j in i:
            b.append(j.categories_id) #Список из статей (Без QuerySet)
    c = []
    for i in set(b):
        c.append(Articles.objects.filter(categories_id=i).order_by('-date'))
    categories = Categories.objects.all()
    return render(request, 'main/index.html', {'recomendations': c, 'categories': categories})



def profile(request):
    prof = Profile.objects.filter(profile_id=request.user.id)
    created_news = Articles.objects.filter(creater_id=request.user.id)
    liked_news = Articles.objects.filter(liked=request.user.id)

    count_like = 0
    for i in created_news:
        get = LikesDislikes.objects.filter(state_like=i.id)
        for j in get:
            if j.like_or_dislike == 'like':
                count_like += 1
    n = Profile.objects.filter(profile_id=request.user.id)
    for i in n:
        bio = i.bio
    else:
        bio = ''
    categories = Categories.objects.all()
    if created_news and liked_news and count_like and prof and bio:
        mid = count_like//(created_news.count())
        return render(request, 'main/profile.html', {'my_news': created_news, 'liked_news': liked_news,
                                                 'count_like': count_like, 'mid': mid, 'prof': prof, 'bio': bio, 'categories': categories})

    else:
        return render(request, 'main/profile.html', {'my_news': created_news, 'liked_news': liked_news,
                                                     'count_like': count_like, 'prof': prof, 'bio': bio, 'categories': categories})