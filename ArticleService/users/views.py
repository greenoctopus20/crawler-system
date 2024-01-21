# pylint: disable=E1101

from .articles_helper import Session, articles
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.core.serializers import serialize
from .rabbitmq import produce_message
from django.forms.models import model_to_dict
import json 
import msgpack
from .models import User, Site
import pickle
from .articles_helper import Session, getArticles , articles




def articles_per_site(request, id):
    
    articles_data = getArticles(id)
    site = Site.objects.get(id=id)
    transformed_data = []
    try:
        for article in articles_data:
            transformed_data.append({
                "url": article.url,
                "title": article.title,
                "body": article.body,
                "author": article.author,
                "date": article.date
            })
    except Exception as E:
        return JsonResponse({"msg" : "something went wrong"}, safe=False, status=500)
    transformed_data.append({"domain" : site.domain_url})

    json_object = json.dumps(transformed_data, indent=4)
    return JsonResponse(json_object, safe=False, status=200)
    
