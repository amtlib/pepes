from django.urls import path, include
from rest_framework import routers
from .api.views import PepeView


router = routers.DefaultRouter()
router.register('pepes', PepeView)


urlpatterns = [
    path('api/', include(router.urls))
]