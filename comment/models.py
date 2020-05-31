from django.db import models
from django.utils import timezone
from blog.models import Post

# Create your models here.

class Comment(models.Model):

    name = models.CharField(max_length=50,verbose_name="名字")
    email = models.EmailField(verbose_name="邮箱")
    url = models.URLField(verbose_name="网址",blank=True)
    text = models.TextField(verbose_name="评论")
    create_time = models.DateTimeField(verbose_name="创建时间",default=timezone.now())
    post = models.ForeignKey("blog.Post",verbose_name="文章",on_delete=models.CASCADE)

    class Meta:
        db_table = "comment"
        verbose_name = "评论"
        verbose_name_plural = verbose_name

    def __str__(self):

        return "{}:{}".format(self.name,self.text[:20])

