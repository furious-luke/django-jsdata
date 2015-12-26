import json

from django.template import Library
from django.utils.html import escapejs
# from django.core.serializers.json import DjangoJSONEncoder
from django.utils.safestring import mark_safe
from rest_framework.renderers import JSONRenderer


register = Library()


@register.filter(is_safe=True)
def jsdata_render(value, name='jsdata_json'):
    data = escapejs(JSONRenderer().render(value))
    return mark_safe('<script>%s = "%s";</script>'%(name, data))


@register.simple_tag(takes_context=True)
def jsdata(context):
    return jsdata_render(context.get('jsdata', ''))
