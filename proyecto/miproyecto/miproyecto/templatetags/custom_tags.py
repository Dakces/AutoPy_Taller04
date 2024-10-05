from django import template
from urllib.parse import urlencode
from django.contrib.auth.models import User,Group

register = template.Library()

@register.simple_tag
def query_transform(request, **kwargs):
    updated = request.GET.copy()
    for k, v in kwargs.items():
        if v is not None:
            updated[k] = v
        else:
            updated.pop(k, 0)

    return updated.urlencode()
    
@register.filter
def get_is_active(value):
    if value:
        return 'Activo'
    else:
        return 'Inactivo'

@register.filter(name='has_group')
def has_group(user, group_name):
    rol = user.groups.all()[0].name[:3]
    return user.groups.filter(name=group_name).exists()
    
@register.filter(name='has_permission_simple')
def has_permission_simple(user, permission):
    role = user.groups.all()[0].name[:3]
    roles = roles_permission.get(permission)
    exist_count = roles.count(role)
    if exist_count > 0:
        return True
    else:
        return False
        
@register.filter(name='has_permission')
def has_permission(user, permission):
    
    print(permission)
    print(user.has_perm(permission))
    if user.has_perm('permission'):
        return True
    else:
        return False