from django.contrib import admin
from .models import Testimonials

class TestimonialsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'full_name',
        'comment',
        'rate',
        'created_at',
    )

    ordering = ('created_at',)

admin.site.register(Testimonials, TestimonialsAdmin)
