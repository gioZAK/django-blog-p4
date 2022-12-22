from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.text import slugify
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from cloudinary.uploader import upload


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def create_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            image_url = None
            if 'featured_image' in request.FILES:
                image_url = upload(request.FILES['featured_image'])['url']
            else:
                image_url = 'placeholder'
            post = form.save(commit=False)
            post.author = request.user
            post.status = 1
            post.slug = slugify(post.title)
            post.featured_image = image_url
            post.save()
            return redirect(reverse('post_detail', args=[post.slug]))
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    # Only allow the post's author to edit the post
    if request.user != post.author:
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            image_url = post.featured_image
            if 'featured_image' in request.FILES:
                image_url = upload(request.FILES['featured_image'])['url']
            post = form.save(commit=False)
            post.author = request.user
            post.status = 1
            post.slug = slugify(post.title)
            post.featured_image = image_url
            post.save()
            return redirect(reverse('post_detail', args=[post.slug]))
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form, 'post': post})


@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    # Only allow the post's author to delete the post
    if request.user != post.author:
        return HttpResponseForbidden()

    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'delete_post.html', {'post': post})


@login_required
def profile(request, username):
    # Get the user whose profile is being viewed
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user)
    # Check if the logged-in user is the owner of the profile
    is_owner = request.user == user
    return render(request, 'profile.html', {'user': user, 'posts': posts,
                                            'is_owner': is_owner})


@login_required
def delete_account(request):
    if request.method == 'POST':
        # Handle form submission
        username = request.POST['username']
        # Get the user object
        user = User.objects.get(username=username)
        # Delete the user's account
        User.objects.filter(username=username).delete()
        # Delete the user's comments
        Comment.objects.filter(name=username).delete()
        # Display a success message
        messages.success(request, f'Account "{username}" was deleted.')
        # Redirect to a home page
        return redirect('home')
    else:
        # Render the delete account template
        return render(request, 'delete_account.html')
