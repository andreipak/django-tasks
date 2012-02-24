from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def admin_path(obj):
    return reverse('admin:%s_%s_change' % (
                    obj._meta.app_label,
                    obj._meta.module_name
                ), args=(obj.id,))


class AdminEditLinkNode(template.Node):
    def __init__(self, obj, label=None):
        self.obj = template.Variable(obj)
        self.label = label

    def render(self, context):
        _object = self.obj.resolve(context)
        path = admin_path(_object)
        label = self.label or u'(admin)'

        return u'<a href="%s">%s</a>' % (path, label)


@register.tag(name="admin_edit_link")
def do_edit_link(parser, token):
    """
    You need to pass in at least an object
    """

    token = token.split_contents()

    try:
        obj = token.pop(1)
    except IndexError:
        raise template.TemplateSyntaxError, \
                '%s tag requires at least an object as first argument' % token[0]

    try:
        label = token.pop(1)
    except IndexError:
        label = None
    return AdminEditLinkNode(obj, label)