'''
Created on May 22, 2013

@author: drelfi
'''

from django.contrib import admin
from garagesale.models import Item, Screenshots, ContactRequest

class ScreenshotsInline(admin.StackedInline):
    model = Screenshots
    extra = 3
    
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [ScreenshotsInline]

class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Item, ItemAdmin)
admin.site.register(ContactRequest, ContactRequestAdmin)
