from django.conf.urls import url,patterns, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'^area',views.PostalCodeViewSet)

urlpatterns = patterns(
    '',
    url(r'^',include(router.urls)),
    #url(r'^facebook-check/$',views.CheckForFacebook.as_view(),name="facebook-check")
)
