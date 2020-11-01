from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.contact_us, name='contact'),
    path('<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
]
