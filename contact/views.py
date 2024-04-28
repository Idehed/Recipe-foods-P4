from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ContactForm


def contact_view(request):
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Thank you for reaching out!"
                " We appreciate your interest and will be in touch shortly. "
                "Best regards, NourishNShare",
            )
            return HttpResponseRedirect(request.path_info)

    else:
        contact_form = ContactForm()
    return render(request, "contact/contact.html",
                  {"contact_form": contact_form})
