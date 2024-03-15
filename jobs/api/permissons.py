from rest_framework import permissions

class IsEmployer(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        print(f"USER = {request.user.userType}")
        return request.user.userType == "Employer"

class IsJobCreatorOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj): 
        if request.method in permissions.SAFE_METHODS:  #safe methods (e.g., GET, HEAD, OPTIONS)
            return True
        return request.user == obj.user #if the requested user is equals to object user

