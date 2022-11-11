import datetime

from django.db import models
from django.contrib.auth.models import User

from register.models import Profile


class Categories(models.Model):
    categories_title = models.CharField('Категория', max_length=30, blank=True, null=True)

    def __str__(self):
        return f'{self.categories_title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Articles(models.Model):

    title = models.CharField('Название', max_length=100)
    anons = models.CharField('Анонс', max_length=150, blank=True, null=True)
    img = models.ImageField(upload_to='images/', blank=True, null=True)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации', blank=True, null=True, auto_now=True)

    categories = models.ForeignKey(Categories, default=7, on_delete=models.CASCADE)

    creater_id = models.IntegerField('Id автора', blank=True, null=True)
    creater_username = models.CharField('Имя автора', blank=True, null=True, max_length=30)


    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author', null=True)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')

    def __str__(self):
        return f'{self.title} Дата: {self.date}'

    def get_absolute_url(self):
        return f'/news/{self.id}'


    @property
    def num_likes(self):
        return self.liked.all().count()

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'



class LikesDislikes(models.Model):

    LIKE_OR_DISLAKE_CHOICES = (
        ("LIKE", "like"),
        ("DISLIKE", "dislike"),
    )

    user_like = models.ForeignKey(User, on_delete=models.CASCADE)
    state_like = models.ForeignKey(Articles, on_delete=models.CASCADE)
    like_or_dislike = models.CharField(max_length=7, choices=LIKE_OR_DISLAKE_CHOICES, null=True, blank=True)

    def __str__(self):
        return f'{self.user_like} {self.state_like}'

    class Meta:
        verbose_name = 'Понравились'
        verbose_name_plural = 'Понравившиеся статьи'

class Comment(models.Model):

    HIDDEN = (
        ("HIDDEN", "hidden"),
        ("SHOW", "show"),
    )

    article = models.ForeignKey(Articles, on_delete=models.CASCADE, null=True, blank=True, related_name='comments_articles')
    commentator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField('Комментарий', max_length=300)
    date = models.DateTimeField('Дата комментария', default=datetime.datetime.now)
    status = models.CharField(verbose_name='', max_length=7, choices=HIDDEN, default='show')

    def __str__(self):
        return f'Комментарий {self.comment} к статье {self.article}'

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'


