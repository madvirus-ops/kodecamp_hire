from django.contrib import admin
from .models import Event, Newsletter,Contact

# Register your models here.
admin.site.register(Newsletter)
admin.site.register(Contact)
admin.site.register(Event)