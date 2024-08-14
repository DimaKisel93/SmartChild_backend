from django.http import JsonResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from SmartChild_backend.settings import FIREBASE_API_KEY, FIREBASE_APP_ID, FIREBASE_AUTH_DOMAIN, FIREBASE_MESSAGING_SENDER_ID, FIREBASE_PROJECT_ID, FIREBASE_STORAGE_BUCKET

@method_decorator(login_required, name='dispatch')
class GetFirebaseConfig(View):
    def get(self, request):
        config = {
            "API_KEY": FIREBASE_API_KEY,
            "AUTH_DOMAIN": FIREBASE_AUTH_DOMAIN,
            "PROJECT_ID": FIREBASE_PROJECT_ID,
            "STORAGE_BUCKET": FIREBASE_STORAGE_BUCKET,    
            "MESSAGING_SENDER_ID": FIREBASE_MESSAGING_SENDER_ID,
            "APP_ID": FIREBASE_APP_ID
        }
        return JsonResponse(config)
