# pylint: disable=E1101


from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.core.serializers import serialize

import json 
from .models import User, Site


def get_sites(request):
    if request.method == 'GET':
        try:
            sites = Site.objects.all().values()
            sites_list = list(sites)  
            return JsonResponse(sites_list, safe=False, status=200)
        except Exception as e:
            print(str(e))
            return JsonResponse({'message': str(e)}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
        
def add_site(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')
            user_id = User.objects.get(pk=1);

            # Create a new Site object linked to the user
            new_site = Site.create(
                user_id=user_id,
                domain_url=data.get('domainURL'),
                article_xpath=data.get('articlesXpath'),
                title_xpath=data.get('title'),
                body_xpath=data.get('body'),
                author_xpath=data.get('author'),
                date_xpath=data.get('date')
            )
            new_site.save()
            data = '{"message": "Site added successfully", "site_id": '+ str(new_site.id) +'}'
            data = json.loads(data)
            return JsonResponse(data=data, status=201)
            
        except Exception as e:
            print(str(e))
            return JsonResponse({'message': str(e)}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
