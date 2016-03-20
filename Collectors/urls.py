from django.conf.urls import url,patterns, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'^area',views.PostalCodeViewSet)
router.register(r'^client',views.ClientsViewSet,base_name='client')
router.register(r'^collecter',views.CollectorsViewSet,base_name='collecter')

urlpatterns = patterns(
    '',
    url(r'^',include(router.urls)),
    url(r'^route/$',views.route.as_view(),name="route")

)
