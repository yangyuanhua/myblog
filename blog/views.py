from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from .models import Post,Category,Tag
import markdown
import re
from markdown.extensions.toc import TocExtension
from django.utils.text import slugify
from django.db.models import Q
from django.views.generic import ListView,DetailView
from django.views.generic.base import View
from  pure_pagination import PaginationMixin
from django.contrib import messages




class IndexView(PaginationMixin,ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "postlist"
    paginate_by = 10

    # def index_view(self,request):
    #     postlist = Post.objects.all().order_by("-create_time")
    #     # for i in postlist:
    #     #     print(i.excerpt)
    #     for post in postlist:
    #         post.count = post.comment_set.all().count()
    #
    #     welcome = "hello world"
    #     title = "我的博客首页"
    #     return render(request,"blog/index.html",locals())
    #     # return HttpResponse("欢迎访问我们的页面")


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/details.html"
    context_object_name = "post"

    def get(self,request,*args,**kwargs):

        response = super(PostDetailView,self).get(request,*args,**kwargs)
        self.object.increase_views()

        return response
    # def get_object(self,queryset=None):
    #
    #     post = super().get_object(queryset=None)
    #     md = markdown.Markdown(extensions=["markdown.extensions.extra",
    #                                        "markdown.extensions.codehilite",
    #                                        TocExtension(slugify=slugify)])
    #     post.body = md.convert(post.body)
    #     post.toc = md.toc
    #     m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    #     post.toc = m.group(1) if m is not None else ''
    #
    #     return post





# def details(request,pk):
#
#     try:
#         post = Post.objects.get(id=pk)
#         post.increase_views()
#         print("*"*100)
#         md = markdown.Markdown(extensions=['markdown.extensions.extra',
#                                            'markdown.extensions.codehilite',
#                                            TocExtension(slugify=slugify)])
#         post.body = md.convert(post.body)
#         post.toc = md.toc
#         # print(post.comment_set().all())
#         post.count = post.comment_set.all().count()
#         m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
#         post.toc = m.group(1) if m is not None else ''
#     except Exception as e:
#         print(e)
#     return render(request,"blog/details.html",locals())




#归档视图
class ArchiveView(View):

    def get(self,request, year, month):

        print("&"*100)

        postlist = Post.objects.filter(create_time__year=year).order_by('create_time')
        postlist = [i for i in postlist if i.create_time.month==int(month) ]
        return render(request, 'blog/index.html', locals())


class CategoryView(IndexView):
    def get_queryset(self):
        try:
            cate = Category.objects.get(pk=self.kwargs.get("pk"))
        except Exception as e:
            print(e)
            return
        return super(CategoryView, self).get_queryset().filter(category=cate)

        # #分类视图
        # def category(request,pk):
        #     try:
        #         cate = Category.objects.get(id=pk)
        #     except Exception as e:
        #         print(e)
        #         return render(request,'blog/404.html')
        #     postlist = Post.objects.filter(category=cate).order_by("create_time")
        #     return render(request,"blog/index.html",locals())


#标签视图
class TagView(IndexView):
    def get_requryset(self):
        tag = get_object_or_404(Tag,pk="pk")
        return super(TagView,self).get_queryset().filter(tag=tag)

    # def tag(request,pk):
    #     try:
    #         tag = Tag.objects.get(id=pk)
    #     except Exception as e:
    #         print(e)
    #         return render(request,'blog/404.html')
    #     postlist = Post.objects.filter(tag=tag).order_by("create_time")
    #
    #     return render(request,"blog/index.html",locals())

#search 视图
def search(request):

    q = request.GET.get("q")

    if not q:
        error_msg="请输入搜索关键词"
        messages.add_message(request, messages.ERROR, error_msg, extra_tags='danger')
        return redirect('blog:index')
    postlist = Post.objects.filter(Q(title__icontains=q)|Q(body__icontains=q))
    return render(request, 'blog/index.html', locals())




