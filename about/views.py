from django.shortcuts import render


def about_index(request):
    from about.models import About
    about = About.objects.all()
    context = {
        'about': about
    }
    return render(request, 'about_index.html', context)
