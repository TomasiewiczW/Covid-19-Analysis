from django.views.generic import TemplateView


# Create your views here.
class WebmapTemplateView(TemplateView):
    template_name = "webmap/map.html"