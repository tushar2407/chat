from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class Contact(models.Model):
    user = models.ForeignKey(User, related_name = 'friends', on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', blank = True)

    def __str__(self):
        return self.user.username

class Message(models.Model):
    contact = models.ForeignKey(Contact, related_name='message', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)
    
    def __str__(self):
        return self.contact.user.username

class Chat(models.Model):
    participant = models.ManyToManyField(Contact, related_name='chats')
    messages = models.ManyToManyField(Message, blank = True)

    def last_10_messages(self):
        return self.messages.objects.all()[:10]
    
    def __str__(self):
        return f"{self.pk}"