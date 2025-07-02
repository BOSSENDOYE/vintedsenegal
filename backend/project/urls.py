from django.contrib import admin
from django.urls import path, include
from .api_home import api_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_home, name='api-home'),
    path('api/users/', include('users.urls')),
    path('api/listings/', include('listings.urls')),
    path('api/transactions/', include('transactions.urls')),
    path('api/messaging/', include('messaging.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('api/notifications/', include('notifications.urls')),
]
