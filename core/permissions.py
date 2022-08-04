from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self,request,view):
        
        admin_permission = bool(request.user and request.user.is_staff)
        return request.method == 'GET' or admin_permission

class DetailPermissionGetOrOnlyAdminOrOnlyWriter(permissions.BasePermission):

    """
    관리자계정(is_staff = True)는 무엇이든 가능
    
    단순 조회는 누구나(비회원 포함) 가능
    
    그 외의 행동은 작성자만 가능
    """

    def has_object_permission(self,request,view,obj):
        return request.user.is_staff or request.method == 'GET' or request.user == obj.user
