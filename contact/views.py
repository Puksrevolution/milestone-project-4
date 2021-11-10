"""
Code adapted from https://github.com/auxfuse/Milestone4
"""

from django.shortcuts import render
from django.contrib import messages
from .models import Contact
from .forms import ContactQuery


def contact(request):
    """
    Render contact template and ContactQuery form. Once form is filled
    out, save and display to the Admin dashboard. If
    user is a registered & logged user we capture their username for the
    admin, otherwise user is public and query_from is left blank.
    """
    if request.method == 'POST':
        create_contact_form = Contact(
            query_title=request.POST.get('query_title'),
            query_text=request.POST.get('query_text'),
            query_email=request.POST.get('query_email'),
            query_from=request.user if request.user.is_authenticated else None
        )
        create_contact_form.save()
        messages.success(request, 'Mail sent. We will be in touch.')

    context = {
        'form': ContactQuery
    }
    return render(request, 'contact/contact.html', context)
