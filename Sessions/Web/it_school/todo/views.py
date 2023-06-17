from django.views.generic import TemplateView
from todo.models import Todo
# Create your views here.
# Class-Based views


class ListAll(TemplateView):

    template_name = "todo/landing.html"
    model = Todo 