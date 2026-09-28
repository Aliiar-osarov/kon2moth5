from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

from notes.views import RegisterView, ProfileView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('notes.urls')),

    path('register/', RegisterView.as_view()),
    path('profile/', ProfileView.as_view()),

    path('login/', TokenObtainPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),

    path('schema/', SpectacularAPIView.as_view()),
    path(
        'swagger/',
        SpectacularSwaggerView.as_view(url_name='schema')
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )