from rest_framework import permissions

# class IsEmployer(permissions.BasePermission):
#     message="Only Employers can post jobs"

#     def has_permission(self, request, view):
#         if request.method == 'POST':
#             user = request.user

#             if user.userType != "Employer":
#                 return False

#         return True


class IsJobCreatorOrEmployer(permissions.BasePermission):
     
    def has_permission(self, request, view): #This is will be trigger on every HTTP REQUEST.
       if request.method == 'POST':
            user = request.user

            if user.userType != "Employer":
                return False

            return True
       else:
        return True

    def has_object_permission(self, request, view, obj):  #POST request will not trigger this permission function.

        if request.method in permissions.SAFE_METHODS:  #safe methods (e.g., GET, HEAD, OPTIONS)
            return True
        return request.user == obj.user #if the requested user is equals to object user

