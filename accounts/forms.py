from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """Custom User Creation Form"""
    
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "username",
            "email", 
            "age",
            #No need for password since it is required
        )

class CustomUserChangeForm(UserChangeForm):
    """Custom User Change Form"""

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email", 
            "age",
        )