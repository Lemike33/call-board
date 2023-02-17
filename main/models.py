from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    """ Description """
    TYPES = (
        ('01', 'Танки'),
        ('02', 'Хилы'),
        ('03', 'ДД'),
        ('04', 'Торговцы'),
        ('05', 'Гилдмастеры'),
        ('06', 'Квестгиверы'),
        ('07', 'Кузнецы'),
        ('08', 'Кожевники'),
        ('09', 'Зельевары'),
        ('10', 'Мастера заклинаний')
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=2, choices=TYPES, default='01')
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.title[:20]} ----> id:{self.id}'


class Comment(models.Model):
    """ Description """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creation = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=960)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.post.title[:20]}'






