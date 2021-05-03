from django.contrib import admin 

from main.models import Chat, Contact, Message

admin.site.register(Chat)
admin.site.register(Message)
admin.site.register(Contact)