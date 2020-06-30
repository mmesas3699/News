from datetime import datetime, timedelta

from rest_framework.response import Response
from rest_framework.views import APIView

from news.settings import collection


class ArticleView(APIView):

    def get(self, request, format=None):
        """Return only the news extracted from twelve hours ago."""
        now = datetime.now()
        hours = timedelta(hours=12)
        limit = now - hours

        pages = list(collection.find({}, {'_id': 0, 'page': 1}).distinct('page'))
        news_list = []
        for page in pages:
            news = {}

            # Get page_url
            page_url = collection.find_one(
                {'page': f'{page}'},
                {'_id': 0, 'page_url': 1}
            )

            # Get articles
            _filter = {'page': f'{page}', 'date': {'$gt': limit}}
            articles = list(collection.find(
                _filter,
                {'_id': 0, 'title': 1, 'link': 1, 'epigraph': 1}
                )
            )

            news['page'] = page
            news['page_url'] = page_url['page_url']
            news['articles'] = articles
            news_list.append(news)

        return Response({'news': news_list})
