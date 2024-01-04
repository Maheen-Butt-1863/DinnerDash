from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from resturant.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["display_name", "email", "username"]


class CustomUserChangeForm(UserChangeForm):
    pass
