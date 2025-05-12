from django.http import HttpResponse


class DoctorLoginRequiredMixin:

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponse("You must be logged in to access this page.")

        if self.request.user.role != "doctor":
            return HttpResponse("You do not have permission to view this page.")

        return super().dispatch(request, *args, **kwargs)
