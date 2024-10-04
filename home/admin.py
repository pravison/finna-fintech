from django.contrib import admin
from . models import CompanyInfor, ContactMessage, About, Service, Team, Testimonial

# Register your models here.
admin.site.register(CompanyInfor)
admin.site.register(ContactMessage)
admin.site.register(About)
admin.site.register(Service)
admin.site.register(Team)
admin.site.register(Testimonial)