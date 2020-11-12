from django.db import models
from django.contrib.auth.models import User
from blog.models import Post


class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    target = models.ForeignKey(Post, verbose_name='评论目标', on_delete=models.DO_NOTHING)
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS)
    content = models.TextField(verbose_name='正文')
    creator = models.ForeignKey(User, verbose_name='作者', on_delete=models.DO_NOTHING, related_name='comment_creator')
    nick_name = models.CharField(max_length=50, verbose_name='昵称')
    email = models.EmailField(verbose_name='邮箱')
    website = models.URLField(verbose_name='网站')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '评论'



