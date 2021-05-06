# from django.db import models

# from django.contrib.auth import get_user_model

# User = get_user_model()

# class Contact(models.Model):
#     user = models.ForeignKey(User, related_name = 'friends', on_delete=models.CASCADE)
#     friends = models.ManyToManyField('self', blank = True)

#     def __str__(self):
#         return self.user.username

# class Message(models.Model):
#     contact = models.ForeignKey(Contact, related_name='message', on_delete=models.CASCADE)
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ('-timestamp',)
    
#     def __str__(self):
#         return self.contact.user.username

# class Chat(models.Model):
#     participant = models.ManyToManyField(Contact, related_name='chats')
#     messages = models.ManyToManyField(Message, blank = True)

#     def last_10_messages(self):
#         return self.messages.objects.all()[:10]
    
#     def __str__(self):
#         return f"{self.pk}"

from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User = get_user_model()

class Contact(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    study = models.TextField(blank=True)
    no = models.CharField(max_length=10,blank=True)
    def _str_(self):
        return self.user.username

    def get_user_contact(username):
        user = get_object_or_404(User, username=username)
        return get_object_or_404(Contact, user=user)

    def _str_(self) -> str:
        return self.user.username

class Message(models.Model):
    contact = models.ForeignKey(Contact,on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.content

class Chat(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    participants = models.ManyToManyField(
        Contact, blank=True)
    messages = models.ManyToManyField(
        Message, blank=True)
    universal_chat = models.BooleanField(default=False)

    class Meta:
        permissions = (
            ('universal', 'Univeral Chat'),
        )
    def _str_(self):
        return "{}".format(self.name)

    def get_last_10_messages(room_name):
        chat = get_object_or_404(Chat, name=room_name)
        return chat.messages.order_by('-timestamp').all()[:10]

    def get_current_chat(room_name):
        return get_object_or_404(Chat, name=room_name)