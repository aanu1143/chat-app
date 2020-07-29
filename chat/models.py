from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q

User = get_user_model()

class Message(models.Model):
    contact = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name="receipant", on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    def last_10_messages(form, to):
        messages = Message.objects.order_by('timestamp').all()
        filterMessages = messages.filter(Q(recipient=form, contact=to) | Q(contact=form, recipient=to))
        leng = len(filterMessages)
        if leng<80:
            return filterMessages
        else:
            return filterMessages[leng-50:]