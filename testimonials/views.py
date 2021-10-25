from django.shortcuts import render

# Create your views here.


def testimonials(request):
    """ A view to return the studio page """

    return render(request, 'testimonials/testimonials.html')
