from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('chat-api/', include('main.api.urls', namespace='chat')),
    path('chat/', include('main.urls')),
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
