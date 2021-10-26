from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Testimonials

from .forms import TestimonialsForm


def testimonials(request):
    """ A view to return the testimonials page """

    testimonials = Testimonials.objects.all()

    if request.method == "POST":
        form = TestimonialsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Testimonial posted successfully!')
        else:
            messages.error(request, 'There is a fault with your form.')
        return redirect(reverse('testimonials'))
    else:
        form = TestimonialsForm()

    template = 'testimonials/testimonials.html'
    context = {
        'testimonials': testimonials,
        'form': form,
    }

    return render(request, template, context)
