from datetime import datetime, timedelta

from rest_framework.response import Response
from rest_framework.views import APIView

from news.settings import collection


class ArticleView(APIView):

    def get(self, request, format=None):
        # Return only the news extracted from twelve hours ago
        now = datetime.now()
        hours = timedelta(hours=12)
        limit = now - hours

        pages = list(collection.find({}, {'_id': 0, 'page': 1}).distinct('page'))
        news = []
        for page in pages:
            filter_ = {'page': f'{page}', 'date': {'$gt': limit}}
            query = list(collection.find(filter_, {'_id': 0}))
            news.append({f'{page}': query})

        return Response({'news': news})
