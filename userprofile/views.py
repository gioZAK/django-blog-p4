from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.text import slugify
from django.views import generic, View
from .models import Post, Comment
from .forms import CommentForm, PostForm


class ProfileView(generic.TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the user whose profile is being viewed
        user = get_object_or_404(User, username=self.kwargs['username'])
        context['user'] = user
        context['posts'] = Post.objects.filter(author=user)
        # Check if the logged-in user is the owner of the profile
        context['is_owner'] = self.request.user == user
        return context


class DeleteAccountView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'delete_account.html'

    def post(self, request, *args, **kwargs):
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
