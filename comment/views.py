from django.shortcuts import render,HttpResponse,redirect
from blog.models import Post
from .forms import CommentForms
from django.views.decorators.http import require_POST
from django.contrib import messages


# Create your views here.

@require_POST
def comment(request,post_pk):
    try:
        post = Post.objects.get(pk=post_pk)
    except Exception as e:
        print(e)
        return render(request,"blog/404.html")
    print(request.POST)
    form = CommentForms(request.POST)
    #检查form表单是否合法
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        messages.add_message(request,messages.SUCCESS,"评论发表成功",extra_tags="sucess")
        url = "/blog/posts/%s"%(post_pk)
        return redirect(url)
    context={"post":post,"form":form}
    messages.add_message(request, messages.ERROR, '评论发表失败！请修改表单中的错误后重新提交。', extra_tags='danger')
    return render(request,"comment/preview.html",locals())
