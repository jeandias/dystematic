from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from apps.stock_sentiment import views

router = routers.DefaultRouter()
router.register(r'companies', views.CompanyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/prices/', views.PriceList.as_view()),
    path('api/recommendations', views.RecommendationList.as_view())
]
