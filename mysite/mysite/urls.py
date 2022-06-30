"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from login import views
from rest_framework.authtoken import views as authViews
from .router import router, gc_router
from login.views import RegisterView,SubmitView



urlpatterns = [
    path('polls/', include('polls.urls')),
    re_path(r'^admin/', admin.site.urls),
    # path('index/', views.index),
    path('login/', views.login),
    # path('register/', views.register),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('logout/', views.logout),
    # path('api/', include('login.urls')),
    path('api/', include(router.urls)),
    path('giftcard/', include(gc_router.urls)),
    path('api-token-auth/', authViews.obtain_auth_token, name='api-token-auth'),
    # giftcard submit
    path('submit/', SubmitView.as_view(), name='auth_register'),
]




# 未登录人员，不论是访问index还是login和logout，全部跳转到login界面
# 已登录人员，访问login会自动跳转到index页面
# 已登录人员，不允许直接访问register页面，需先logout
# 登出后，自动跳转到login界面

