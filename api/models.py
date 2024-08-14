from django.db import models

class FirebaseConfig(models.Model):
    api_key = models.CharField(max_length=255)
    auth_domain = models.CharField(max_length=255)
