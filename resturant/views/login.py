from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse


class CustomLoginView(LoginView):
    def form_valid(self, form):
        response = super().form_valid(form)

        if self.request.user.is_staff:
            return redirect(reverse("admin_dashboard"))
        else:
            return redirect(reverse("home"))
