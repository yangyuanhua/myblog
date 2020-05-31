from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
import markdown
from django.utils.html import strip_tags
from markdown.extensions.toc import TocExtension
import re
from django.utils.functional import cached_property


# Create your models here.



class Category(models.Model):

    name = models.CharField(max_length=100,verbose_name="分类名")

    class Meta:
        db_table = "category"
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):

        return self.name

class Tag(models.Model):

    name = models.CharField(max_length=100,verbose_name="标签名")

    class Meta:
        db_table = "tag"
        verbose_name = "标签"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Post(models.Model):

    title = models.CharField(max_length=70,verbose_name="标题")
    body = models.TextField(verbose_name="内容")
    create_time = models.DateTimeField(verbose_name="创建时间",default=timezone.now)
    modified_time = models.DateTimeField(verbose_name="修改时间")
    excerpt = models.CharField(max_length=200,blank=True)
    view = models.PositiveIntegerField(default=0,editable=False,verbose_name="浏览量")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="类别外键")
    tag = models.ManyToManyField(Tag,verbose_name="标签外键")
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    class Meta:
        db_table = "post"
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ["-create_time"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        md = markdown.Markdown(extensions=["markdown.extensions.extra",'markdown.extensions.codehilite',])
        self.excerpt = strip_tags(md.convert(self.body))[:54]

        super().save(*args, **kwargs)

    #每浏览一次加1
    def increase_views(self):

        self.view += 1
        self.save(update_fields=["view"])

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数

    #reverse反向解析“blog:details"前面'blog'是app名字,后面details是urls.py后面name=”details"
    def get_absolute_url(self):

        return reverse("blog:details", kwargs={"pk": self.pk})


    @property
    def toc(self):
        return self.rich_content.get("toc", "")

    @property
    def body_html(self):
        return self.rich_content.get("content", "")

    @cached_property
    def rich_content(self):
        return generate_rich_content(self.body)



def generate_rich_content(value):
    md = markdown.Markdown(
        extensions=[
            "markdown.extensions.extra",
            "markdown.extensions.codehilite",
            # 记得在顶部引入 TocExtension 和 slugify
            TocExtension(slugify=slugify),
        ]
    )
    content = md.convert(value)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    toc = m.group(1) if m is not None else ""
    return {"content": content, "toc": toc}









