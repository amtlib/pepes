from django.urls import path, include
from rest_framework import routers
from .api.views import PepeView
from .views import IndexView


router = routers.DefaultRouter()
router.register('pepes', PepeView)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/', include(router.urls))
]