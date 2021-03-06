from django.shortcuts import render
from django.contrib import messages

from .models import Testimonials
from .forms import TestimonialsForm


def testimonials(request):
    """ A view to return the testimonials page and/or add testimonials """

    testimonials = Testimonials.objects.all()
    user = request.user

    if request.method == "POST":
        form = TestimonialsForm(request.POST)
        if form.is_valid():
            full_name = request.POST.get('full_name')
            rate = request.POST.get('rate')
            comment = request.POST.get('comment')
            Testimonials(full_name=full_name, user=user, rate=rate,
                         comment=comment).save()
        else:
            messages.error(request, 'Failed to add testimonial. \
                           Please ensure the form is valid.')
    else:
        form = TestimonialsForm()

    template = 'testimonials/testimonials.html'

    context = {
        'testimonials': testimonials,
        'form': form,
    }

    return render(request, template, context)
