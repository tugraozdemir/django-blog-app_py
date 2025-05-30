# article/urls.py

from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('addarticle/',views.addArticle,name = "addarticle"),
    path('article/<slug:slug>/',views.detail,name = "detail"),
    path('update/<slug:slug>',views.updateArticle,name = "update"),
    path('delete/<slug:slug>',views.deleteArticle,name = "delete"),
    path('',views.articles,name = "articles"), # articles/ altındaki ana makale listesi
    path('comment/<slug:slug>',views.addComment,name = "comment"),
]