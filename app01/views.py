from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import datetime
from django.template.loader import get_template
from .models import Article
from .models import Category
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

# def index(request):
#     template = get_template('index.html')
#     return render(request, 'index.html')
#

def new_list(request):
    # all_article = Article.objects.all()
    # return render(request, './post/list.html', {'all_article': all_article})
    all_article = Article.objects.all()
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(all_article, per_page=5, request=request)
    all_article = p.page(page)

    return render(request, './post/list.html', {'all_article': all_article})


def post_list(request):
    # article_list = Article.objects.all()
    # archive_list = []
    # for article in article_list:
    #     # 将每一个文章的发布日期都获取出来，按照'%Y/%m'进行格式化
    #     pub_date = article.pub_date.strftime('%Y')
    #     if pub_date not in archive_list:
    #         # 如果这个时间字符串不在article_list这个列表中，就把这个年月添加进去
    #         archive_list.append(pub_date)
    # posts = archive_list
    #
    #
    # return render(request, './post/post.html', {'posts': posts})
    # article_list = Article.objects.order_by("pub_date__year")
    article_list = Article.objects.all()
    return render(request, './post/post.html', {'article_list': article_list})


def all_list(request):
    all_article = Article.objects.all()
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(all_article, per_page=1, request=request)
    all_article = p.page(page)
    ctx = {
        'all_article': all_article,

    }
    return render(request, './post/all.html', ctx)


def blog_detail(request, bid):
    post = Article.objects.get(id=bid)
    post.save()
    # 博客标签
    ctx = {
        'post': post,

    }
    return render(request, './post/show.html', ctx)


# def blog_tags(request, cid=-1):
#     post_list = None
#     if cid != -1:
#        cat = Article.objects.get(id=cid)
#        post_list = cat.post_set.all()
#     else:
#        post_list = Post.objects.all()
#
#     ....
#
#     ctx = {
#         'post_list': post_list,
#         'tags': tag_message_list
#     }
#     return render(request, 'list.html', ctx)

def category(request):
    blogcategory_list = Category.objects.all()
    return render(request, './post/tags.html', {'blogcategory_list': blogcategory_list})


def category_list(request, tid):
    # tag = Category.objects.get(id=tid)

    article_list = Article.objects.filter(category=tid).order_by('-pub_date')
    return render(request, './post/taglist.html', {'article_list': article_list})


# def page_not_found(request, exception, template_name='./post/404.html'):
#     return render(request, './post/404.html')
def projects(request):
    return render(request, './post/projects.html')

def about(request):
    return render(request, './post/about.html')
