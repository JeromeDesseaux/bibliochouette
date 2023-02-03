from django.contrib import admin
from .models import Holder, HolderGroup

# Register your models here.
admin.site.register(Holder)
admin.site.register(HolderGroup)
