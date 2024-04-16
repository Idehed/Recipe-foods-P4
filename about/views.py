from django.views.generic import TemplateView

def about_me(request):
    """
    Make the About page run
    """
    about = About.objects.all().order_by('-updated_on').first()

    request render(
        request,
        "about/about.html"
        {"about": about},
    )