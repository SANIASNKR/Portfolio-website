from django.db import models

class Contact(models.Model):
    # Name field with a higher max length for flexibility
    name = models.CharField(max_length=100)
    
    # Email field with a longer max length to handle longer email addresses
    email = models.EmailField(max_length=254)
    
    # Phone number field (optional, in case international formats are needed)
    phone = models.CharField(max_length=15, blank=True, null=True)
    
    # Subject (as a choice field to match the form options)
    SUBJECT_CHOICES = [
        ('General Inquiry', 'General Inquiry'),
        ('Project Collaboration', 'Project Collaboration'),
        ('Feedback', 'Feedback'),
        ('Others', 'Others'),
    ]
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES, default='General Inquiry')
    
    # Message field for the user's message (text area)
    message = models.TextField()
    
    # Timestamp to track when the form was submitted
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"

    