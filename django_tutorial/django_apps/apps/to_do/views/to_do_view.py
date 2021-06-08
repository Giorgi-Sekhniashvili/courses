from django.views.generic import TemplateView


class ToDoView(TemplateView):
    template_name = 'to_do/to_do.html'
