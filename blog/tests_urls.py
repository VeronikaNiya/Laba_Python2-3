from django.test import TestCase
from django.urls import reverse, resolve

from .views import HomePageView
from .views import ArticleDetail


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/blog/')
        self.assertEquals(view.func.view_class, HomePageView)

    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args=('name',))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_article_list(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_article_detail(self):
        view = resolve('/blog/articles/<2021>/<04>/<28>/<detective>')
        self.assertEquals(view.func.view_class, ArticleDetail)

