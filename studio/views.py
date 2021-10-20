from django.shortcuts import render

# Create your views here.


def studio(request):
    """ A view to return the studio page """

    return render(request, 'studio/studio.html')
