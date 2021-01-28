from django.http import request
from django.http.response import Http404, HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from .models import Tweet
from .forms import TweetForm
from .serializers import TweetSerializer, serializers
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hellow World</h1>")
    return render (request,"pages/home.html", context = {}, status = 200)

def tweet_detail_view(request, tweet_id, *args , **kwargs):
    """
    REST API VIEW 
    Consume by JavaScript  
    return json data 
    """
    data = {
        "id": tweet_id,
        #image also
    }
    status = 200
    try:
        obj = Tweet.objects.get(id = tweet_id)
        data["content"] = obj.content
    except: 
        data["content"] = "Not found"
        status = 404
    return JsonResponse(data, status = status)


def tweet_list_view (request, *args, **kwargs):
    """
    REST API VIEW 
    Consume by JavaScript  
    return json data 
    """
    tweet_list = Tweet.objects.all()
    data_list = [{"id": t.id,"content": t.content, "likes": 0} for t in tweet_list]
    data = {
        "isUser": False ,
        "response": data_list
    }
    return JsonResponse(data_list,safe= False)

def tweet_create_view (request,*args,**kwargs):
    """
    REST API CREATE VIEW 
    """
    serializer = TweetSerializer(data = request.POST or None)
    if serializer.is_valid():
        obj =serializer.save(user = request.user)
        return JsonResponse(serializer.data, status = 201)  

    return JsonResponse({}, status = 400)



def tweet_create_view_caca (request, *args, **kwargs):
    """
    REST API CREATE VIEW 
    """
    form = TweetForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit = False)
        obj.save()
        form = TweetForm()
    return render(request, 'components/forms.html', context = {"form" : form})