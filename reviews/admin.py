"""
Code adapted from https://github.com/BrianWhelanDublin/milestone-project-4
"""

from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    readonly_fields = (
        'reviewer',
        'review',
        'stars',
        )


admin.site.register(Review, ReviewAdmin)
