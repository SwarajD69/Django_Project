from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Skill, Hero, About

def home(request):
    # Fetch all content
    projects = Project.objects.all()
    skills = Skill.objects.all()
    hero = Hero.objects.first()  # Hero section
    about = About.objects.first()  # About Me section

    if request.method == "POST":
        # Handle contact form submission
        name = request.POST.get("name")
        email = request.POST.get("email")
        message_text = request.POST.get("message")

        full_message = f"Message from {name} ({email}):\n\n{message_text}"

        try:
            # Send email (optional, requires email backend configured)
            send_mail(
                subject=f"Portfolio Contact Form: {name}",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],  # change to your email
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, "Sorry, your message could not be sent. Try again later.")

        # Redirect to the same page and stay at contact section
        return redirect(request.path + "#contact")

    return render(request, "portfolio/home.html", {
        "projects": projects,
        "skills": skills,
        "hero": hero,
        "about": about
    })
