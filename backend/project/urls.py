from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .api_home import api_home

urlpatterns = [
    path('admin/', admin.site.urls),
    # URLs des applications API (doivent être avant api_home)
    path('api/users/', include('users.urls')),
    path('api/listings/', include('listings.urls')),
    path('api/transactions/', include('transactions.urls')),
    path('api/messaging/', include('messaging.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('api/notifications/', include('notifications.urls')),
    # Page d'accueil de l'API (doit être en dernier)
    path('api/', api_home, name='api-home'),
]

# Servir les fichiers media en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
