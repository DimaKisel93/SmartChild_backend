from django.urls import path
from .firebase_views import GetFirebaseConfig

urlpatterns = [
    path('get-firebase-config/', GetFirebaseConfig.as_view(), name='get-firebase-config'),
]