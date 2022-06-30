from login.views import userviewsets,giftcardviewsets
from rest_framework import routers
 
router = routers.DefaultRouter()
router.register('user', userviewsets, basename ='user_api')

gc_router = routers.DefaultRouter()
gc_router.register('giftcard', giftcardviewsets, basename ='user_api')
