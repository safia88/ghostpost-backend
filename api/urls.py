from api.views import PostViewSet
from rest_framework.routers import DefaultRouter
from django.conf.urls import include, url

router = DefaultRouter()

router.register(r'post', PostViewSet)

urlpatterns = [
    url('', include(router.urls)),
    url('api/', include(router.urls))
]
