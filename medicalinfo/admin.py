from django.contrib import admin
from .models import Doctor
from .models import Medicine

admin.site.register(Doctor)
admin.site.register(Medicine)