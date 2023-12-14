from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            l = len(message.split(" "))
            return render(request, "success.html", {"length": l})
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})
