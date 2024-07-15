"""
URL configuration for news_search project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from search import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.search_news, name='search_news'),
    path('results/<int:search_id>/', views.search_results, name='search_results'),
    path('previous_searches/', views.previous_searches, name='previous_searches'),
    path('refresh/<int:search_id>/', views.refresh_results, name='refresh_results'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]





