from django import template

from pythonz import VERSION


register = template.Library()


@register.simple_tag
def pythonz_version():
    """Возвращает версию проекта.

    :return:
    """
    return '.'.join(map(str, VERSION))
