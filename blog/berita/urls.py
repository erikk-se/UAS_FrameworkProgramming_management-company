from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView # type: ignore

router = DefaultRouter()
router.register(r'company', views.CompanyViewSet)

urlpatterns = [
    path('<str:company_slug>/', views.company, name='company'),
    path('', views.index),
    path('', include(router.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)