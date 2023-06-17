from django.views.generic import TemplateView

# Create your views here.
# Class-Based views


class LandingPage(TemplateView):

    template_name = "base/index.html" 