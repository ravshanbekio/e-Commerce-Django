from django.db import models
from account.models import Account

class Contact(models.Model):
    client = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.message