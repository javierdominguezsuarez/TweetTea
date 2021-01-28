from django.http import request
from django.http.response import Http404, HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view  
from rest_framework.response import Response
from .models import Tweet
from .forms import TweetForm
from .serializers import TweetSerializer, serializers

def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hellow World</h1>")
    return render (request,"pages/home.html", context = {}, status = 200)

#Using old django


def tweet_detail_view_old(request, tweet_id, *args , **kwargs):
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

def tweet_list_view_old (request, *args, **kwargs):
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

def tweet_create_view_old (request, *args, **kwargs):
    """
    REST API CREATE VIEW 
    """
    form = TweetForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit = False)
        obj.save()
        form = TweetForm()
    return render(request, 'components/forms.html', context = {"form" : form})

# Using django rest framework

@api_view(['GET'])
def tweet_detail_view (request,tweet_id,  *args, **kwargs):
    obj = Tweet.objects.get(id = tweet_id)
    if not obj.exists():
        return Response({}, status = 404)
    obj = obj.first()
    serializer = TweetSerializer(obj)
    return Response(serializer.data, status = 200)

@api_view(['GET'])
def tweet_list_view (request, *args, **kwargs):
    tweet_list = Tweet.objects.all()
    serializer = TweetSerializer(tweet_list, many = True)
    return Response(serializer.data, status = 200)



@api_view(['POST'])
def tweet_create_view (request,*args,**kwargs):
    """
    REST API CREATE VIEW 
    """
    serializer = TweetSerializer(data = request.POST or None)
    if serializer.is_valid():
        serializer.save(user = request.user)
        return Response(serializer.data, status = 201)  

    return Response({}, status = 400)
