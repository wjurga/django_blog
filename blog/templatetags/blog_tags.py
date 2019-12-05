from django import template

register = template.Library()

from ..models import Post


@register.inclusion_tag('blog/latest_posts.html')
def show_latest_post(count=5):
    latest_post = Post.objects.order_by('-date_posted')[:count]
    return {'latest_post': latest_post}