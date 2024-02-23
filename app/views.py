from django.shortcuts import render, redirect
from app.models import Case
from app.forms import ContactForm

def index(request):
    cases = Case.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank-you-contact')
    else:
        form = ContactForm()

    return render(request, 'app/index.html', {'cases': cases, 'form': form})

def thank_you_contact(request):
    return render(request, 'app/pages/thank-you-contact.html')

# from django.shortcuts import render

# def index(request):
#     return render(request, 'app/index.html')