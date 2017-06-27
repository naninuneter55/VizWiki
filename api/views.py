import json
import re
from collections import OrderedDict
from django.http import HttpResponse
from visualization.models import Material
from visualization.models import Sparql
from django.template.loader import get_template
from django.template import Template
from django.template import Context


def query(request, material_id):
    material = Material.objects.get(pk=material_id)
    res = Sparql.query(material)
    # print("$$$ {} $$$".format(res['results']['bindings']))
    meta = json.loads(material.meta)
    # print("$$$ {} $$$".format(meta))

    items = []
    for result in res['results']['bindings']:
        od = []
        for key, value in result.items():
            v = value['value']
            if key in meta['split_columns']:
                w = v.split('__')
                if w[0]:
                    v = w[0]

            # print("### {} ###".format(value['value']))
            od.append((key, v))
        items.append(OrderedDict(od))

    #template = get_template("api/{}.txt".format(material.template))
    template = Template(meta['comment_template'])
    ct = Context({ 'items': items, 'meta': meta })
    comment = template.render(ct)
    # comment = ""
    # print(comment)

    # print("$$$ {} $$$".format(meta))
    # print("$$$ {} $$$".format(items))
    # print("$$$ {} $$$".format(comment))
    data = OrderedDict([('meta', meta), ('comment', comment),('items', items)])
    return render_json_response(request, data)

def render_json_response(request, data, status=None):
    """response を JSON で返却"""
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    # print("$$$ {} $$$".format(json_str))
    callback = request.GET.get('callback')
    if not callback:
        callback = request.POST.get('callback')  # POSTでJSONPの場合
    if callback:
        json_str = "%s(%s)" % (callback, json_str)
        response = HttpResponse(json_str, content_type='application/javascript; charset=UTF-8', status=status)
    else:
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status)
    return response

def conv(s):
    cs = []
    for e in re.findall("&#x([0-9a-fA-F]+);", s):
        cs.append(chr(int(e, 16)))
    return "".join(cs)
