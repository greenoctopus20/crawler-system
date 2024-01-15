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
    
    articles_data = getArticles(1)  # Assuming '1' is the site_id

    transformed_data = []
    for article in articles_data:
        transformed_data.append({
            "url": article.url,
            "body": article.body,
            "author": article.author,
            "date": article.date
        })

    json_object = json.dumps(transformed_data, indent=4)
    return JsonResponse(json_object, safe=False, status=200)
    

def get_overview():
    data = []
    sites = Site.objects.all()
    for site in sites:
        tmp = {
            "id" : site.id,
            "domain" : site.domain_url,
            "articlesExtracted" : 0,
            "failedArticles" : 0, 
            "lastExtracted" : "2023-12-14",
        }
        data.append(tmp)
    return data

def get_sites(request):
    if request.method == 'GET':
        try:    
            data = get_overview()
            json_object = json.dumps(data, indent = 4)
            return JsonResponse(json_object, safe=False, status=200)
        except Exception as e:
            print(str(e))
            return JsonResponse({'message': str(e)}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
        
def add_site(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            #user_id = data.get('user_id')  # Assuming this is the ID of the user
            user_id = 1
            # Fetch the User object based on the user_id
            user = User.objects.get(pk=user_id)

            # Create a new Site object linked to the user
            new_site = Site.objects.create(
                user=user,
                domain_url=data.get('domainURL'),
                article_xpath=data.get('articlesXpath'),
                title_xpath=data.get('title'),
                body_xpath=data.get('body'),
                author_xpath=data.get('author'),
                date_xpath=data.get('date')
            )

            data = {
                "message": "Site added successfully",
                "site_id": new_site.id
            }
            return JsonResponse(data=data, status=201)
            
        except Exception as e:
            print(str(e))
            return JsonResponse({'message': str(e)}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)


def run(request):
    site = Site.objects.get(id=9)
    data = model_to_dict(site)
    data = pickle.dumps(data)
    produce_message(data)
    return JsonResponse({'message': 'testing'}, status=200)

def runSite(request, id):
        if request.method in ['POST', 'GET'] and id is not None:
            try:               
                target = Site.objects.get(id=id)
                processSite(target)
                return JsonResponse({"message": "Site is running "}, status=200)
            except Exception as E:
                print(E)
                return JsonResponse({'message': 'Failled to run site'}, status=500)
        else:
            return JsonResponse({'message': 'Method not allowed'}, status=500)
            
def deleteSite(request, id):
    try:
        if request.method in ['POST', 'GET'] and id is not None:
            print(id)
            try:
                target = Site.objects.get(id=id)
                target.delete()
                return JsonResponse({'message': 'Site is Deleted'}, status=200)
            except Exception as E:
                print(E)
                return JsonResponse({'message': "something wrong"}, status=500)
        else: 
            return JsonResponse({'message': 'Method not allowed'}, status=500)
    except Exception as E:
        print(E)
        return JsonResponse({'message': E}, status=500)
   
def processSite(site):
    data = model_to_dict(site)
    data = pickle.dumps(data)
    produce_message(data)
    