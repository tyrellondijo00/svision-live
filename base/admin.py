from django.contrib import admin

# Register your models here.
from .models import Client, Member, Project, Testimony,Service

admin.site.register(Client)
admin.site.register(Member)
admin.site.register(Project)
admin.site.register(Testimony)
admin.site.register(Service)
