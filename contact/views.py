from django.shortcuts import render, redirect
from django.contrib import message
from django.http import HttpResponseRedirect
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        contact_form = ContactForm(data.request.POST)
        if contact_form.is_valid():
            contact_form.save()
            message.add_message(request, message.SUCCESS, "Hi, Thank you for reaching out! This is to confirm that we have received your form submission. "
            " We appreciate your interest and will be in touch shortly. "
            "Best regards, NourishNShare")
            return HttpResponseRedirect(request.path_info)

        else:
            contact_form = ContactForm()
        return render (request,'contact.html', {'contact_form': contact_form})

