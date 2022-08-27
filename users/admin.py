from django.contrib import admin
from users.models import CybersafeModel, Phonenumber,VendorModel,CybersafeModel,Profile
# Register your models here.
admin.site.register(Phonenumber)
admin.site.register(VendorModel)
admin.site.register(CybersafeModel)
admin.site.register(Profile)