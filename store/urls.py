from store.views import CustomerViewSet, OrderViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'Customers', CustomerViewSet)
router.register(r'Orders', OrderViewSet)

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('', include(router.urls)),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
