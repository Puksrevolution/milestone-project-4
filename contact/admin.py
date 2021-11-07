from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    readonly_fields = (
        'query_title',
        'query_text',
        'query_email',
        'date_posted',
        'query_from',
        )


admin.site.register(Contact, ContactAdmin)
