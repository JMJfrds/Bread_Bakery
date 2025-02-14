from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.conf import settings
from django.urls import reverse_lazy
from bv1.forms import ContactForm
from bv1.models import ContactModel


class HomeView(TemplateView):
    template_name = 'bv1/index.html'


class AboutView(TemplateView):
    template_name = 'bv1/about.html'


class ServiceView(TemplateView):
    template_name = 'bv1/service.html'


class ProductView(TemplateView):
    template_name = 'bv1/product.html'


class TeamView(TemplateView):
    template_name = 'bv1/team.html'


class TestimonialView(TemplateView):
    template_name = 'bv1/testimonial.html'


class SuccesView(TemplateView):
    template_name = 'bv1/succes.html'


class ContactView(View):
    template_name = 'bv1/contact.html'

    def get(self, request):
        form = ContactForm()
        return render(request, 'bv1/contact.html', {'form': form})
    
    def post(self, request):
        form = ContactForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            print(f"Form is valid: Name: {name}, Email: {email}, Phone: {phone}, Message: {message}")
            return redirect("succes")
        else:
            print("Form is not valid")
            print(form.errors)
            return render(request, 'bv1/contact.html', {'form': form})