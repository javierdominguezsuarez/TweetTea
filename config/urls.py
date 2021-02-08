"""tweetme2 URL Configuration
"""
#from django.conf import settings
from django.conf.urls.static import static
from account.views import ProfileViewSet
from django.conf.urls import include
from tweets.views import TweetViewSet
from tweets.views import home_view
#from tweets.views import tweet_detail_view, tweet_list_view, tweet_create_view,tweet_delete_view
from django.contrib import admin
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router2 = routers.DefaultRouter()

router.register('tweets', TweetViewSet)
router2.register('profiles', ProfileViewSet)
api = [
    path('', include('account.urls')),
    path('', include(router.urls)),
    path('',include(router2.urls))
    ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('v1/',include(api))
]

#if settings.DEBUG == True:
  #  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)