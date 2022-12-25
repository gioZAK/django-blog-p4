from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.text import slugify
from django.views import generic, View
from .models import Post, Comment
from .forms import CommentForm, PostForm


class PostList(generic.ListView):
    """
    The PostList view allows the user to view a paginated list of post
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(generic.DetailView):
    """
    The PostDetail view allows the user to view the post page itself,
    displaying post, likes, comments
    """
    model = Post
    template_name = 'post_detail.html'
    queryset = Post.objects.filter(status=1)

    # This method get data and add it if there is a comment or like
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(
            approved=True
            ).order_by("-created_on")
        context['commented'] = False
        context['liked'] = self.object.likes.filter(
            id=self.request.user.id
            ).exists()
        context['comment_form'] = CommentForm()
        return context

    # This method post comment and check the like status
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


class PostLike(generic.RedirectView):
    """
    The PostLike view allows the user to view the post itself
    """
    permanent = False
    query_string = True

    # Allows the user to like and unlike
    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, slug=kwargs['slug'])
        if post.likes.filter(id=self.request.user.id).exists():
            post.likes.remove(self.request.user)
        else:
            post.likes.add(self.request.user)
        return reverse('post_detail', kwargs={'slug': post.slug})


class PostCreateView(generic.CreateView):
    """
    The PostCreateView view allows the user to create a new blog post
    """
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'

    # This method post the form and display a success message
    def form_valid(self, form):
        # Set the author and status of the post
        form.instance.author = self.request.user
        form.instance.status = 1
        form.instance.slug = slugify(form.instance.title)
        # Save the post and redirect to the success URL
        response = super().form_valid(form)
        messages.success(
            self.request, f'Post "{form.instance}" created successfully'
            )
        return response

    # This method determines the url of the created post
    def get_success_url(self):
        # Get the slug of the post that was just created
        slug = self.object.slug
        return reverse('post_detail', args=[slug])


class PostEditView(generic.UpdateView):
    """
    The PostEditView allows the user to edit his post.
    """
    model = Post
    form_class = PostForm
    template_name = 'edit_post.html'

    # Save the post and redirect to the post detail page
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request, f'Post "{form.instance}" updated successfully'
            )
        return response

    # This method determines the url
    def get_success_url(self):
        return reverse('post_detail', args=[self.object.slug])


class PostDeleteView(generic.DeleteView):
    """
    The PostDeleteView deletes the and redirects the user to the home page
    """

    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    # This method gets the user response and display a message.
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(request, f'Post "{self.object}" deleted successfully')
        return response
