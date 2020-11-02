from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm, NoteForm, forms 

# Create your views here.
def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, "contacts/list_contacts.html",
                  {"contacts": contacts})


def add_contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/add_contact.html", {"form": form})

def add_note(request, pk):
    contact = get_object_or_404(Contact, pk=pk) 
    if request.method =="POST":
      form = NoteForm(data=request.POST)
      if form.is_valid():
        note = forms.save(commit=False)
        note.contact=contact
    return redirect(to="contact_detail", pk=pk)


def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'GET':
        form = ContactForm(instance=contact)
    else:
        form = ContactForm(data=request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/edit_contact.html", {
        "form": form,
        "contact": contact
    })


def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect(to='list_contacts')

    return render(request, "contacts/delete_contact.html",
                  {"contact": contact})
    

      
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method =='GET':
        form = NoteForm()
    return render(request, "contacts/contact_detail.html", #3part thing leading to the next step
            {"contact": contact})