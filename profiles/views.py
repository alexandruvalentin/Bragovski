from django.shortcuts import (
    render, redirect, reverse, get_object_or_404
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from testimonials.models import Testimonials
from testimonials.forms import TestimonialsForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
        else:
            messages.error(request, 'Update failed.'
                           'Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    testimonials = request.user.testimonials.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'testimonials': testimonials,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def edit_testimonial(request, testimonial_id):
    """
    Edit a testimonial on your profile
    """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    testimonial = get_object_or_404(Testimonials, pk=testimonial_id)
    if request.method == 'POST':
        form = TestimonialsForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated testimonial!')
            return redirect(reverse('profile'))
        else:
            messages.error(request, 'Failed to add testimonial. \
                           Please ensure the form is valid.')
    else:
        form = TestimonialsForm(instance=testimonial)
        messages.info(request, 'You are editing your testimonial.')

    template = 'profiles/edit_testimonial.html'
    context = {
        'form': form,
        'testimonial': testimonial,
    }

    return render(request, template, context)


@login_required
def delete_testimonial(request, testimonial_id):
    """
    Delete testimonial from the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    testimonial = get_object_or_404(Testimonials, pk=testimonial_id)
    testimonial.delete()
    messages.success(request, 'Testimonial deleted!')
    return redirect(reverse('profile'))


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation mail was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
