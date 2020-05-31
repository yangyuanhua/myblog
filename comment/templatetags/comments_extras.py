from django import template
from ..forms import CommentForms


register = template.Library()

@register.inclusion_tag("comment/inclusions/_form.html",takes_context=True)
def show_comment_form(context,post,form=None):
    if form is None:
        form = CommentForms
    return {"form":form,"post":post}

@register.inclusion_tag('comment/inclusions/_list.html', takes_context=True)
def show_comments(context, post):
    comment_list = post.comment_set.all().order_by('-create_time')
    comment_count = comment_list.count()
    return {
        'comment_count': comment_count,
        'comment_list': comment_list,
    }