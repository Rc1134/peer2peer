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
from home.models import ProfileId


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

    all_posts = Post.objects.all().order_by('-timeStamp')
    paginator = Paginator(all_posts, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    logger.info(f"Retrieved {all_posts.count()} posts")

    context = {'page_obj': page_obj, 'form': form}
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
    likes_count = post.likes.count() if post.likes.exists() else 0  
    comments_count = comments.count() if comments.exists() else 0 
    bookmark_count=post.bookmark.count() if post.bookmark.exists() else 0

    context={'post':post, 'comments': comments, 'user': request.user, 'likes_count':likes_count ,'comments_count':comments_count,'bookmark_count':bookmark_count, 'replyDict': replyDict}
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
        comment_text = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get('parentSno')
        parent = None if parentSno == "" else dcomment.objects.get(sno=parentSno)
        image = request.FILES.get('image')  
        file = request.FILES.get('file')

        if not comment_text and not file:
            messages.warning(request, "You must provide a comment text or upload a file.")
            return redirect(f"/blog/{post.slug}")

        new_comment = dcomment(
            comment=comment_text,
            user=user,
            post=post,
            parent=parent,
            image=image,
            file=file
        )
        new_comment.save()
        if parent:
            messages.success(request, "Your reply has been posted successfully")
        else:
            messages.success(request, "Your comment has been posted successfully")
        
        return redirect(f"/blog/{post.slug}")
    