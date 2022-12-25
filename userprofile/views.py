from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from blog.models import Post, Comment
from django.db.models.signals import post_save
from django.dispatch import receiver
from .forms import ProfileForm
from .models import Profile


# Receiver created in order to create a profile for the user after register
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class ProfileView(generic.TemplateView):
    """
    The ProfileView view allows the user to view profiles
    """
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
    """
    The DeleteAccountView view allows the user delete his profile
    """
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


class EditProfileView(View):
    """
    The EditProfileView view allows the user edit his profile
    """
    def get(self, request, username):
        # Get the user object
        user = get_object_or_404(User, username=username)

        # Check if the logged-in user is the owner of the profile
        if request.user != user:
            # If the logged-in user is not the owner, display an error message
            messages.error(request, 'You are not allowed.')
            # Redirect the user back to the home page
            return redirect('home')

        form = ProfileForm(instance=user.profile)
        return render(request, 'edit_profile.html', {'form': form,
                                                     'username': username})

    def post(self, request, username):
        # Get the user object
        user = get_object_or_404(User, username=username)

        form = ProfileForm(request.POST, request.FILES, instance=user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was updated successfully!')
            return redirect(reverse('profile', args=[username]))
