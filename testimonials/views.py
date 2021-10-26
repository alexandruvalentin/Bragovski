from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Testimonials
from .forms import TestimonialsForm


def testimonials(request):
    """ A view to return the testimonials page and/or add testimonials """

    testimonials = Testimonials.objects.all()
    user = request.user

    if request.method == "POST":
        form = TestimonialsForm(request.POST)
        full_name = request.POST.get('full_name')
        rate = request.POST.get('rate')
        comment = request.POST.get('comment')
        Testimonials(full_name=full_name, user=user, rate=rate,
                     comment=comment).save()
    else:
        form = TestimonialsForm()

    template = 'testimonials/testimonials.html'

    context = {
        'testimonials': testimonials,
        'form': form,
    }

    return render(request, template, context)
