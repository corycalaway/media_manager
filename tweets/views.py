from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Tweet
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h1>Hello Wooooorrrrrrrlllllldddddd!!!!!!!<h1>")

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    print(args, kwargs)
    """
    REST API VIEW
    Consume by Javascript
    return json data
    """
    try:
        obj = Tweet.objects.get(id=tweet_id)
    except:
        raise Http404
    # return HttpResponse(f"<h1>Hello {tweet_id} - {obj.content}!<h1>")
    

    data = {

    }

    return JsonResponse(data)