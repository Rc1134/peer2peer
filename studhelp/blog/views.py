from venv import logger
from django.shortcuts import render, HttpResponseRedirect , get_object_or_404 , redirect 
import logging
from blog.models import Post , dcomment , PostForm
from django.contrib import messages
from django.utils.text import slugify
from blog.templatetags import extras
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.paginator import Paginator


def blogHome(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            title = form.cleaned_data['title']
            author = request.user

            slug = slugify(title)
            original_slug = slug
            counter = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1

            post = Post(content=content, slug=slug, title=title, author=author)
            post.save()
            messages.success(request, "Your post has been saved successfully!")
            return redirect('blogHome')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PostForm()

    allPosts = Post.objects.all().order_by('-timeStamp')
    logger.info(f"Retrieved {allPosts.count()} posts")
    context = {'allPosts': allPosts, 'form': form}
    return render(request, 'blog/bloghome.html', context)





def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    comments= dcomment.objects.filter(post=post, parent=None).order_by('-timeStamp')
    replies= dcomment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, 'likes_count':post.likes.count() , 'replyDict': replyDict}
    return render(request, "blog/blogPost.html", context)

def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blogpost', args=[post.slug]))

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        if comment == "":
            messages.warning(request, "Fill comment")
        else:
            parentSno= request.POST.get('parentSno')
            if parentSno=="":
                comment=dcomment(comment= comment, user=user, post=post)
                comment.save()
                messages.success(request, "Your comment has been posted successfully")
            else:
                parent= dcomment.objects.get(sno=parentSno)
                comment=dcomment(comment= comment, user=user, post=post , parent=parent)
                comment.save()
                messages.success(request, "Your reply has been posted successfully")
        
        return redirect(f"/blog/{post.slug}")
    


def article_list(request):
    all_posts = Post.objects.all()

    paginator = Paginator(all_posts, 10) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/bloghome.html', {'page_obj': page_obj})



