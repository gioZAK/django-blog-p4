from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('create/', views.PostCreateView.as_view(), name='create_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('edit/<slug:slug>/', views.PostEditView.as_view(), name='edit_post'),
    path('delete/<slug:slug>/', views.PostDeleteView.as_view(), name='delete_post'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]