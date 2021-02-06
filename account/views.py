
from rest_framework.decorators import action
from account.models import FollowerRelation, Profile
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.views import APIView
from .serializers import ProfileSerializer, UserSerializer, RegisterSerializer
from django.contrib.auth import get_user_model, login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
User =  get_user_model()
# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.save()
        
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class ProfileAPI(APIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_permissions(self):
        if self.request == 'post':
            self.permission_classes =[permissions.IsAuthenticated]
        else :
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()

    def get (self,request,user_id ,*args, **kwargs):
        try:
            obj = Profile.objects.get(id =user_id)
            if  obj == None:
                return Response({}, status = 404)
            serializer = ProfileSerializer(obj)
            return Response(serializer.data, status = 200)
        except:
            return Response({})

    def post (self,request,user_id ,*args, **kwargs):
        obj = User.objects.get(id =user_id)
        if  obj == None:
            return Response({}, status = 404)
        serializer = ProfileSerializer(data = request.data )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = 201)  
    
class ListProfiles(APIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get(self,request,*args, **kwargs):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles,many = True)
        return Response(serializer.data,status = 200)


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    authenticatedActions = ['create','update','partial_update','destroy']
    def get_permissions(self):
        if self.action in self.authenticatedActions:
            self.permission_classes =[permissions.IsAuthenticated]
        else :
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()

    def get_queryset(self):
        try:
            profile =  Profile.objects.filter(user = self.request.user.id)
            pro = profile.first()
            following = pro.followers.all()
            return following
        except: 
            return Profile.objects.all()

    @action (detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def follow (self,request, pId):
        try :
            user = self.request.user
            profile = Profile.objects.get(user = user)
            profileToFollow = Profile.objects.filter(id = pId).first()
            #FollowerRelation.objects.create(profile = profileToFollow)
            profile.followers.add(profileToFollow)
        except :
            return Response({"error":"no se ha podido hacer el follow"},404)