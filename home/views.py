from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact  # Import your Contact model

# Home page view
def home(request):
    return render(request, 'home.html')  # Ensure this template exists

# About page view
def about(request):
    return render(request, 'about.html')  # Ensure 'about.html' exists

# Project page view
def project(request):
    return render(request, 'project.html')  # Ensure 'project.html' exists

# Contact page view
def contact_view(request):
    if request.method == "POST":
        # Retrieving form data from POST request
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('emailInput')
        subject = request.POST.get('exampleSelect')
        message = request.POST.get('exampleTextarea')
        
        # Create and save the Contact instance to the database
        contact_instance = Contact(
            name=name,
            phone=phone,
            email=email,
            subject=subject,
            message=message
        )
        contact_instance.save()  # Save the contact instance to the database
        
        # Respond with a success message
        return HttpResponse("Thank you for reaching out! We will get back to you soon.")
    
    # If GET request, render the contact page
    return render(request, 'contact.html')
