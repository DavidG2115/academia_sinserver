from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg bg-light fs-6'}),
        help_text="La contraseña debe tener al menos 8 caracteres y contener al menos un número.",
        validators=[validate_password],
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control form-control-lg bg-light fs-6', 'placeholder': 'Usuario'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control form-control-lg bg-light fs-6', 'placeholder': 'Confirmar Contraseña'})

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields
        

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)