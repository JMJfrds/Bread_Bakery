from django.contrib import admin
from bv1.models import ContactModel

admin.site.register(ContactModel)

# @admin.register(ContactModel)
# class COntactAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'phone', 'message']