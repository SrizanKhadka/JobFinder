from rest_framework import permissions

class IsEmployer(permissions.BasePermission):
    message="Only Employers can post jobs"

    def has_permission(self, request, view):
        if request.method == 'POST':
            user = request.user

            if user.userType != "Employer":
                return False

        return True


class IsJobCreator(permissions.BasePermission):

    def has_object_permission(self, request, view, obj): 
        if request.method in permissions.SAFE_METHODS:  #safe methods (e.g., GET, HEAD, OPTIONS)
            return True
        return request.user == obj.user #if the requested user is equals to object user

