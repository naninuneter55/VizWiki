from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from visualization.models import Material
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView

class MeterialList(ListView):
    context_object_name='materials'
    template_name='visualization/index.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        materials = Material.objects.order_by('id')
        self.object_list = materials
        context = self.get_context_data(object_list=self.object_list)
        return self.render_to_response(context)

def detail(request, material_id):
    material = get_object_or_404(Material, pk=material_id)
    template = "visualization/{}.html".format(material.template)
    return render(request, template, {'material': material})
