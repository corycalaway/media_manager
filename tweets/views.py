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

     data = {
        "id": tweet_id,
        
        #"image_path": obj.image.url
    }

    status = 200

    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404
    # return HttpResponse(f"<h1>Hello {tweet_id} - {obj.content}!<h1>")

    return JsonResponse(data, status=status) # json.dumps content_type='application/json'