from datetime import datetime

from django.db import models
from django.urls import reverse


def default_datetime(): return datetime.now()


class Article(models.Model):
    title = models.CharField(u'Назва публікації', max_length=25, help_text=u'Максимум 25 символів', default='назва')
    pub_date = models.DateTimeField(u'Дата', default=default_datetime)
    slug = models.SlugField(u'Слаг', default='novels')
    description = models.CharField(u'Опис', max_length=1250, help_text=u'Максимум 1250 символів', default='детектив')

    class Meta:
        verbose_name = u'Публікації'
        verbose_name_plural = u'Назва для публікацій'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "articles/{}/{}/{}/{}".format(self.pub_date.year, self.pub_date.month, self.pub_date.day, self.slug)
    # @property
    # def get_absolute_url(self):
    #
    #     try:
    #         url = reverse('article_detail',
    #                       kwargs={'year': self.pub_date.year, 'month': self.pub_date.month, 'day': self.pub_date.day,
    #                               'slug': self.slug})
    #     except:
    #         url = "/blog/articles/2021/04/29/novels"
    #     return url


class Category(models.Model):
    category = models.CharField(u'Категорія', max_length=250, help_text=u'Максимум 250 символів')
    slug = models.SlugField(u'Слаг')
    objects = models.Manager()

    class Meta:
        verbose_name = u'Категорія для публікації'
        verbose_name_plural = u'Категорії для публікацій'

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        try:
            url = reverse('articles-category-list', kwargs={'slug': self.slug})
        except:
            url = "/"
        return url
