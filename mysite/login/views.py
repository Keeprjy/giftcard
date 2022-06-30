import email
import json
from telnetlib import STATUS
from django.http import JsonResponse

from requests import Response, request
from . import forms
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework import generics
from . import models
from . import serializers
from rest_framework import viewsets
# from login.serializers import UserSerializer, giftcardSerializer
from login.models import User, giftcard
from django.views.decorators.csrf import csrf_exempt
from .serializers import userSerializers, giftcardSerializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
import json


class userviewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializers

class giftcardviewsets(viewsets.ModelViewSet):
    queryset = giftcard.objects.all()
    serializer_class = giftcardSerializers


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        print("RegisterView create " + json.dumps(request.data))
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        print("token res " + "\n" + "true" if created else "false")
        return JsonResponse({
            # "user": serializer.validate_data,
            "token": token.key,
        })



class SubmitView(generics.CreateAPIView):
    queryset = models.giftcard.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = giftcardSerializers

    def create(self, request, *args, **kwargs):
        print("RegisterView create " + json.dumps(request.data))
        serializer = giftcardSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        giftcard = serializer.save()
        return JsonResponse({
            "giftcard": serializer.data,
        })



    # def perform_create(self, serializer):
    #     print("RegisterView perform_create ")
    #     user = serializer.save()
    #     token, created = Token.objects.get_or_create(user=user)
    #     print("token res " + "\n" + "true" if created else "false")
    #     return JsonResponse({
    #         # "user": serializer.validate_data,
    #         "token": token.key,
    #     })

   
    #     Token.objects.create(user=super(RegisterView, self).create(request, *args, **kwargs))

    
# 教科书
# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         return redirect('/index/')
#     else:
#         # Return an 'invalid login' error message.
#         return redirect('/login/')

# def logout_view(request):
#     logout(request)
#     return redirect('/index/')


# Create your views here.
# class PostList(generics.ListAPIView):
#     queryset = models.User.objects.all()
#     serializer_class = serializers.UserSerializer

# class PostDetail(generics.RetrieveAPIView):
#     queryset = models.User.objects.all()
#     serializer_class = serializers.UserSerializer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.User.objects.all()
#     serializer_class = serializers.UserSerializer




# class UserViewSet(viewsets.ModelViewSet):
#     authentication_classes = []
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
# # request 可加回
#     def get_queryset(self):
#         print("UserViewSet list")
#         return super().get_queryset()

#     # @csrf_exempt
#     def create(self, request):
#         print("UserViewSet create")
#         return super().create(request)

#     # @csrf_exempt
#     def perform_create(self, request):
#         print("UserViewSet perform_create")
#         return super().create(request)

    # @csrf_exempt
    # def update(self, request, pk=None):
    #     print("UserViewSet update")
    #     pass

# class giftcardViewSet(viewsets.ModelViewSet):
#     queryset = giftcard.objects.all()
#     serializer_class = giftcardSerializer
# # request 可加回
#     def get_queryset(self):
#         return super().get_queryset()

#     def create(self, request):
#         return super().create(request)

#     def perform_create(self, request):
#         print("UserViewSet perform_create")
#         return super().create(request)




# def index(request):
#     pass
#     return render(request,'login/index.html')
# def index(request):
#     if not request.session.get('is_login', None):
#         return redirect('/login/')
#     return render(request, 'login/index.html')

# def login(request):
#     if request.session.get('is_login', None):  # 不允许重复登录
#         return redirect('/index/')
#     if request.method == 'POST':
#         login_form = forms.UserForm(request.POST)
#         message = 'Check context'
#         if login_form.is_valid():
#             username = login_form.cleaned_data.get('email')
#             password = login_form.cleaned_data.get('password')

#             try:
#                 user = models.User.objects.get(name=email)
#             except :
#                 message = 'No user'
#                 return render(request, 'login/login.html', locals())

#             if user.password == password:
#                 request.session['is_login'] = True
#                 request.session['user_id'] = user.id
#                 request.session['user_name'] = user.email
#                 return redirect('/index/')
#             else:
#                 message = 'Wrong password'
#                 return render(request, 'login/login.html', locals())
#         else:
#             return render(request, 'login/login.html', locals())

#     login_form = forms.UserForm()
#     return render(request, 'login/login.html', locals())

# def register(request):
#     if request.session.get('is_login', None):
#         return redirect('/index/')

#     if request.method == 'POST':
#         register_form = forms.RegisterForm(request.POST)
#         message = "check information"
#         if register_form.is_valid():
#             username = register_form.cleaned_data.get('email')
#             password1 = register_form.cleaned_data.get('password1')
#             password2 = register_form.cleaned_data.get('password2')
#             email = register_form.cleaned_data.get('email')

#             if password1 != password2:
#                 message = 'different password'
#                 return render(request, 'login/register.html', locals())
#             else:
#                 same_name_user = models.User.objects.filter(name=email)
#                 if same_name_user:
#                     message = 'user exist'
#                     return render(request, 'login/register.html', locals())


#                 new_user = models.User()
#                 new_user.name = email
#                 new_user.password = password1
#                 new_user.email = email
#                 new_user.save()

#                 return redirect('/login/')
#         else:
#             return render(request, 'login/register.html', locals())
#     register_form = forms.RegisterForm()
#     return render(request, 'login/register.html', locals())

# def logout(request):
#     if not request.session.get('is_login', None):
#         # 如果本来就未登录，也就没有登出一说
#         return redirect("/login/")
#     request.session.flush()
#     # 或者使用下面的方法
#     # del request.session['is_login']
#     # del request.session['user_id']
#     # del request.session['user_name']
#     return redirect("/login/")

