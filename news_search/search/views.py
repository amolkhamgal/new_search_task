from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Search, SearchResult
from .forms import SearchForm
import requests
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm


@login_required
def search_news(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            search, created = Search.objects.get_or_create(user=request.user, keyword=keyword)

            if created or search.results.count() == 0:
                response = requests.get(f'https://newsapi.org/v2/everything?q={keyword}&apiKey={settings.NEWS_API_KEY}')
                articles = response.json().get('articles', [])
                for article in articles:
                    SearchResult.objects.create(
                        search=search,
                        title=article['title'],
                        description=article['description'],
                        url=article['url'],
                        published_at=article['publishedAt']
                    )

            return redirect('search_results', search_id=search.id)
    else:
        form = SearchForm()

    return render(request, 'search/search.html', {'form': form})

@login_required
def search_results(request, search_id):
    search = Search.objects.get(id=search_id, user=request.user)
    results = search.results.all().order_by('-published_at')

    return render(request, 'search/results.html', {'search': search, 'results': results})

@login_required
def previous_searches(request):
    searches = Search.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'search/previous_searches.html', {'searches': searches})

@login_required
def refresh_results(request, search_id):
    search = Search.objects.get(id=search_id, user=request.user)
    last_published_at = search.results.order_by('-published_at').first().published_at

    response = requests.get(f'https://newsapi.org/v2/everything?q={search.keyword}&from={last_published_at}&apiKey={settings.NEWS_API_KEY}')
    articles = response.json().get('articles', [])
    for article in articles:
        SearchResult.objects.create(
            search=search,
            title=article['title'],
            description=article['description'],
            url=article['url'],
            published_at=article['publishedAt']
        )

    return redirect('search_results', search_id=search.id)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
