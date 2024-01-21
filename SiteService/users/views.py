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
from .articles_helper import count_articles, get_date_last_extracted



def delete_user_data(username):
    try:
        user = User.objects.get(username=username)
        # Unlink data
        user.username = "unknown" # 
        user.save()
    except User.DoesNotExist:
        return True

def delete_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        delete_user_data(data['username'])
        return JsonResponse({'message': 'deleted'}, status=200)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
    
    
def check_username(username):
    try:
        user = User.objects.get(username=username)
        if user:
            return False # user exist no need to sync
    except User.DoesNotExist:
        new_user = User(username=username)
        new_user.save()
        return True
    
def get_user_by_id(id):
    try:
        return User.objects.get(id=id)
    except User.DoesNotExist:
        print("User Doesn't exist")
        return None

def sync_username(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        #print(data['username'])
        print(check_username(data['username']))
        return JsonResponse({'message': 'sync'}, status=200)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)

def get_id_of_user(username):
    try:
        user = User.objects.get(username=username)
        return user.id
    except User.DoesNotExist:
        return None


def get_overview(user):
    data = []
    try:
        if user.username is not "unknown":
            sites = Site.objects.filter(user_id=user.id)
            for site in sites:
                last = get_date_last_extracted(site.id)
                tmp = {
                    "id" : site.id,
                    "domain" : site.domain_url,
                    "articlesExtracted" : count_articles(site.id),
                    "failedArticles" : "0", 
                    "lastExtracted" : str(last) if last else "Not Yet",
                }
                data.append(tmp)
        return data
    except Site.DoesNotExist:
        return data
    
def get_sites(request, username):
    if request.method == 'GET':
        try:
            id = get_id_of_user(username)
            user = get_user_by_id(id)
            if id:
                data = get_overview(user)
                json_object = json.dumps(data, indent = 4)
                return JsonResponse(json_object, safe=False, status=200)
            else:
                return JsonResponse({'msg' : 'user Not found'}, safe=False, status=404)
        except Exception as e:
            print(str(e))
            return JsonResponse({'message': str(e)}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
        
def add_site(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = data['username']
            id = get_id_of_user(username=user)
            
            # Fetch the User object based on the user_id
            user = User.objects.get(pk=id)

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


def Anonymize_User_Data(username):

    id = get_id_of_user(username=username)
    if id:
        print("ID is valid")
        # call functions that delete sites and articles 
    else:
        #return 422
        return None
    