from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from apps.stock_sentiment import views

router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
router.register(r'prices', views.PriceViewSet)
router.register(r'recommendations', views.RecommendationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
