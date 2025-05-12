from django.shortcuts import render
from django.views.generic import TemplateView


class BloomsOverview(TemplateView):
    template_name = "blooms/overview/index.html"


#
