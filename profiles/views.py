from django.views.generic import TemplateView
from .models import Profile

class Profiles(TemplateView):
    """
    User Profile View
    """
    template_name = "profiles/profile.html"

    def get_context_date(self, **kwargs):
        profile = Profile.object.get(user=self.kwargs["pk"])
        context = {
            'profile': profile
        }

        return context