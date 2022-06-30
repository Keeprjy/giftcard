# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.PostList.as_view()),
#     path('<int:pk>/', views.PostDetail.as_view()),
# ]

from django.urls import include, path
from rest_framework import routers
from login.views import UserViewSet, giftcardviewsets
from login.views import MyObtainTokenPairView, RegisterView, SubmitView

router = routers.DefaultRouter()
router.register(r'User', UserViewSet)

gc_router = routers.DefaultRouter()
gc_router.register(r'giftcard', giftcardviewsets)
# router.register(r'giftcard', giftcardViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('giftcard/', include(gc_router.urls)),
   path('register/', RegisterView.as_view(), name='auth_register'),
   # ???
   path('submit/', SubmitView.as_view(),name = 'auth_register'),
]


