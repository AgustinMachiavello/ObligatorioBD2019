# Django
from django.views.generic import TemplateView

# Shortcuts
from django.shortcuts import render

# Utils
from ..utils import get_static_url


class PreviewRouteTemplateView(TemplateView):
    template_name = 'preview_route.html'

    def get(self, request, *args, **kwargs):
        args = {'STATIC_URL': get_static_url()}
        return render(request, self.template_name, args)


class ReversePreviewRouteTemplateView(TemplateView):
    template_name = 'preview_route.html'

    def get(self, request, *args, **kwargs):
        args = {'STATIC_URL': get_static_url()}
        return render(request, self.template_name, args)