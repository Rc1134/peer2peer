from django.shortcuts import render

from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from blog.models import Post

def bookmark_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.bookmark.filter(id=request.user.id).exists():
        post.bookmark.remove(request.user)
        messages.success(request, "Bookmark removed.")
    else:
        post.bookmark.add(request.user)
        messages.success(request, "Post bookmarked successfully.")
    
    return HttpResponseRedirect(reverse('blogpost', args=[post.slug]))



from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def view_bookmarks(request):
    bookmarked_posts = request.user.bookmarked_posts.all().order_by('-timeStamp')
    
    context = {'bookmarked_posts': bookmarked_posts}
    return render(request, 'blog/bookmark.html', context)
