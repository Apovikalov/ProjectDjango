from django.contrib.auth.models import Group, Permission

moderator_group = Group.objects.create(name='Модератор продуктов')

delete_permission = Permission.objects.get(codename='delete_modelname')
unpublish_permission = Permission.objects.get(codename='can_unpublish_product')

moderator_group.permissions.add(delete_permission, unpublish_permission)
