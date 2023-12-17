# pylint: disable=E1101


from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.core.serializers import serialize
from .rabbitmq import produce_message
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
